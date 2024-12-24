from utils.utils import get_model
from rest_framework.serializers import ModelSerializer, SerializerMethodField
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
    project_manager = RelatedUserSerializer(read_only=True)
    team_lead = RelatedUserSerializer(read_only=True)
    assigned_users = RelatedUserSerializer(many=True, read_only=True)

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

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            breakpoint()
            raise ValidationError({"detail": "Project already exists"})


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
            if "project" not in self.initial_data:
                raise ValidationError({"detail": "Project is required"})
            validated_data["project_id"] = self.initial_data["project"]
            return super().create(validated_data)
        except IntegrityError:
            raise ValidationError({"detail": "Task already exists"})


class ActivitySerializer(DynamicFieldsBaseSerializer, ModelSerializer):
    project = RelatedProjectSerializer(read_only=True)
    task = RelatedTaskSerializer(read_only=True)
    user = RelatedUserSerializer(read_only=True)
    duration = SerializerMethodField()

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

    def get_duration(self, obj):
        from ast import literal_eval

        if obj.activity_type == Choices.TIMER_PROGRESS:
            return (
                obj.duration + (now() - obj.modified).total_seconds()
                if isinstance(obj.duration, (int, float))
                else literal_eval(obj.duration) + (now() - obj.modified).total_seconds()
            )
        return obj.duration

    def create(self, validated_data):
        try:
            validated_data["user"] = self.context["request"].user
            validated_data["project_id"] = self.initial_data["project"]
            validated_data["task_id"] = self.initial_data["task"]
            return super().create(validated_data)
        except IntegrityError:
            raise ValidationError({"detail": "Activity already exists"})

    def update(self, instance, validated_data):
        instance.duration = self.initial_data.get("duration", instance.duration)
        instance.save(update_fields=["duration"])
        return super().update(instance, validated_data)
