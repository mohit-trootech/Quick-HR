from utils.utils import get_model
from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    Serializer,
    IntegerField,
    CharField,
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
from django.db import transaction

Project = get_model(app_name="project", model_name="Project")
Task = get_model(app_name="project", model_name="Task")
Activity = get_model(app_name="project", model_name="Activity")
User = get_model(app_name="users", model_name="User")


class AssignedUserSerializer(Serializer):
    assigned_users = CharField(required=True)

    def validate(self, attrs):
        return super().validate(attrs)

    def update(self, instance, validated_data):
        print([id for id in validated_data["assigned_users"].split(",")])
        instance.assigned_users.set(
            [
                id
                for id in validated_data["assigned_users"].split(",")
                if id not in [",", ""]
            ]
        )
        instance.save()
        return instance


class ProjectManagerTeamLeadSerializer(Serializer):
    project_manager_id = IntegerField(required=True)
    team_lead_id = IntegerField(required=True)

    def validate_project_manager(self, value):
        try:
            User.objects.get(id=value)
            return value
        except User.DoesNotExist:
            raise ValidationError({"project_manager": AuthMessage.USER_NOT_EXISTS})

    def validate_team_lead(self, value):
        try:
            User.objects.get(id=value)
            return value
        except User.DoesNotExist:
            raise ValidationError({"team_lead": AuthMessage.USER_NOT_EXISTS})


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
    project_manager = RelatedUserSerializer(read_only=True)
    team_lead = RelatedUserSerializer(read_only=True)
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
            with transaction.atomic():
                assigned_users = self.initial_data.get("assigned_users", None)
                if not assigned_users:
                    ValidationError(
                        {"assigned_users": AuthMessage.ASSIGNED_USERS_IS_REQUIRED}
                    )
                serializer_data = ProjectManagerTeamLeadSerializer(
                    data=self.initial_data
                )
                serializer_data.is_valid(raise_exception=True)
                validated_data["project_manager_id"] = serializer_data.validated_data[
                    "project_manager_id"
                ]
                validated_data["team_lead_id"] = serializer_data.validated_data[
                    "team_lead_id"
                ]
                instance = super().create(validated_data)
                instance.assigned_users.set(
                    [id for id in assigned_users.split(",") if id not in [",", ""]]
                )
                instance.save()
                return instance
        except ValidationError as err:
            raise ValidationError({"detail": str(err)})
        except IntegrityError:
            raise ValidationError({"detail": AuthMessage.PROJECT_EXISTS})


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
