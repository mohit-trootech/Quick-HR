from rest_framework.serializers import BaseSerializer, ModelSerializer
from utils.utils import get_model

User = get_model(app_name="users", model_name="User")
Project = get_model(app_name="project", model_name="Project")
Task = get_model(app_name="project", model_name="Task")


class DynamicFieldsBaseSerializer(BaseSerializer):
    def __init__(self, *args, **kwargs):
        fields = kwargs.pop("fields", None)
        super(DynamicFieldsBaseSerializer, self).__init__(*args, **kwargs)
        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)


class RelatedUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "get_full_name", "image", "is_verified"]


class RelatedProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = [
            "id",
            "title",
            "status",
        ]


class RelatedTaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = [
            "id",
            "title",
            "description",
            "priority",
        ]
