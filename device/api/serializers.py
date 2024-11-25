from rest_framework.serializers import ModelSerializer
from utils.serailizers import DynamicFieldsBaseSerializer, RelatedUserSerializer
from utils.utils import get_model

User = get_model(app_name="users", model_name="User")


class DeviceSerializer(DynamicFieldsBaseSerializer, ModelSerializer):
    acquired_by = RelatedUserSerializer(read_only=True)

    class Meta:
        model = User
        fields = (
            "id",
            "title",
            "slug",
            "description",
            "created",
            "modified",
            "acquired_by",
            "status",
        )
        read_only_fields = ("id", "slug", "created", "modified")
        depth = True
