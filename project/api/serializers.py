from utils.utils import get_model
from rest_framework.serializers import ModelSerializer
from utils.serailizers import (
    DynamicFieldsBaseSerializer,
    RelatedUserSerializer,
    RelatedProjectSerializer,
)

Project = get_model(app_name="project", model_name="Project")
Task = get_model(app_name="project", model_name="Task")


class ProjectSerializer(DynamicFieldsBaseSerializer, ModelSerializer):
    project_manager = RelatedUserSerializer(many=True)
    team_lead = RelatedUserSerializer(many=True)
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
        )
        read_only_fields = ("id", "created", "modified")

    depth = True


class TaskSerializer(DynamicFieldsBaseSerializer, ModelSerializer):
    assigned_user = RelatedUserSerializer(read_only=True)
    project = RelatedProjectSerializer(read_only=True)

    class Meta:
        model = Task
        fields = (
            "id",
            "title",
            "description",
            "project",
            "assigned_user",
            "status",
            "priority",
            "created",
            "modified",
        )
        read_only_fields = ("id", "created", "modified")
