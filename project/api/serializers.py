from utils.utils import get_model
from rest_framework.serializers import ModelSerializer
from utils.serailizers import (
    DynamicFieldsBaseSerializer,
    RelatedUserSerializer,
    RelatedProjectSerializer,
    RelatedTaskSerializer,
)
from django.db.utils import IntegrityError
from rest_framework.exceptions import ValidationError
from django.utils.timezone import now
from project.constants import Choices

Project = get_model(app_name="project", model_name="Project")
Task = get_model(app_name="project", model_name="Task")
Activity = get_model(app_name="project", model_name="Activity")


class ProjectSerializer(DynamicFieldsBaseSerializer, ModelSerializer):
    project_manager = RelatedUserSerializer()
    team_lead = RelatedUserSerializer()
    assigned_users = RelatedUserSerializer(many=True)

    class Meta:
        model = Project
        fields = (
            "id",
            "title",
            "description",
            "status",
            "created",
            "modified",
            "project_manager",
            "team_lead",
            "assigned_users",
            "created_ago",
            "deadline",
            "tasks",
        )
        read_only_fields = ("id", "created", "modified", "created_at")
        depth = True


class TaskSerializer(RelatedTaskSerializer, DynamicFieldsBaseSerializer):
    project = RelatedProjectSerializer(read_only=True)

    class Meta(RelatedTaskSerializer.Meta):
        fields = (
            "id",
            "title",
            "description",
            "project",
            "status",
            "priority",
            "created",
            "modified",
        )
        read_only_fields = ("created", "modified")

    def create(self, validated_data):
        try:
            validated_data["project_id"] = self.initial_data["project"]
            return super().create(validated_data)
        except IntegrityError:
            raise ValidationError({"detail": "Task already exists"})


class ActivitySerializer(DynamicFieldsBaseSerializer, ModelSerializer):
    project = RelatedProjectSerializer(read_only=True)
    task = RelatedTaskSerializer(read_only=True)
    user = RelatedUserSerializer(read_only=True)

    class Meta:
        model = Activity
        fields = (
            "id",
            "project",
            "task",
            "user",
            "activity_type",
            "created",
            "modified",
            "duration",
            "created_ago",
        )
        read_only_fields = ("created", "modified", "created_ago")

    def create(self, validated_data):
        try:
            validated_data["user"] = self.context["request"].user
            validated_data["project"] = Project.objects.get(
                id=self.initial_data["project"]
            )
            validated_data["task"] = Task.objects.get(id=self.initial_data["task"])
            return super().create(validated_data)
        except IntegrityError:
            raise ValidationError({"detail": "Activity already exists"})

    def update(self, instance, validated_data):
        if validated_data["activity_type"] == Choices.TIMER_PAUSE:
            validated_data["duration"] = (now() - instance.modified).total_seconds()
        if validated_data["activity_type"] == Choices.TIMER_START:
            validated_data["activity_type"] = Choices.TIMER_PROGRESS
            validated_data["duration"] = (
                instance.duration + (now() - instance.created).total_seconds()
            )
        return super().update(instance, validated_data)
