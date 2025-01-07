from utils.utils import get_model
from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    Serializer,
    IntegerField,
)
from utils.serailizers import (
    DynamicFieldsBaseSerializer,
    RelatedUserSerializer,
    RelatedProjectSerializer,
    RelatedTaskSerializer,
)
from django.db.utils import IntegrityError
from rest_framework.exceptions import ValidationError
from django.utils.timezone import now
from project.constants import Choices, AuthMessage
from technology.api.serializers import TechnologySerializer

Project = get_model(app_name="project", model_name="Project")
Task = get_model(app_name="project", model_name="Task")
Activity = get_model(app_name="project", model_name="Activity")


class ProjectTaskSerializer(Serializer):
    """Project Task Serializer for Validation"""

    project = IntegerField(required=True)
    task = IntegerField(required=True)

    def validate_project(self, value):
        try:
            Project.objects.get(id=value)
            return value
        except Project.DoesNotExist:
            raise ValidationError({"project": AuthMessage.PROJECT_NOT_EXISTS})

    def validate_task(self, value):
        try:
            Task.objects.get(id=value)
            return value
        except Task.DoesNotExist:
            raise ValidationError({"task": AuthMessage.TASK_NOT_EXISTS})


class ProjectSerializer(DynamicFieldsBaseSerializer, ModelSerializer):
    project_manager = RelatedUserSerializer()
    team_lead = RelatedUserSerializer()
    assigned_users = RelatedUserSerializer(many=True, read_only=True)
    technologies = TechnologySerializer(many=True, read_only=True)
    tasks = RelatedTaskSerializer(many=True, read_only=True)

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
            "technologies",
        )
        read_only_fields = ("id", "created", "modified", "created_at")
        depth = True

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise ValidationError({"project": AuthMessage.PROJECT_EXISTS})


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
                raise ValidationError({"project": AuthMessage.PROJECT_IS_REQUIRED})
            validated_data["project_id"] = self.initial_data["project"]
            return super().create(validated_data)
        except IntegrityError:
            raise ValidationError({"detail": AuthMessage.TASK_EXISTS})


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
            serializer = ProjectTaskSerializer(data=self.initial_data)
            serializer.is_valid(raise_exception=True)
            validated_data["project_id"] = serializer.validated_data["project"]
            validated_data["task_id"] = serializer.validated_data["task"]
            return super().create(validated_data)
        except IntegrityError:
            raise ValidationError({"detail": AuthMessage.ACTIVITY_EXISTS})

    def update(self, instance, validated_data):
        instance.duration = self.initial_data.get("duration", instance.duration)
        instance.save(update_fields=["duration"])
        return super().update(instance, validated_data)
