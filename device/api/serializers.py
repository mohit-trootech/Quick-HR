from rest_framework.serializers import ModelSerializer
from utils.serailizers import DynamicFieldsBaseSerializer, RelatedUserSerializer
from utils.utils import get_model
from markdown import markdown
from device.constants import Choices

Device = get_model(app_name="device", model_name="Device")
User = get_model(app_name="users", model_name="User")


class DeviceSerializer(DynamicFieldsBaseSerializer, ModelSerializer):
    acquired_by = RelatedUserSerializer(read_only=True)

    class Meta:
        model = Device
        fields = (
            "id",
            "title",
            "slug",
            "description",
            "organization",
            "created",
            "modified",
            "acquired_by",
            "status",
        )
        read_only_fields = ("id", "slug", "created", "modified", "organization")
        depth = True

    def update(self, instance, validated_data):
        if "action" in self.context["request"].query_params:
            if self.context["request"].query_params.get("action") == "acquire":
                validated_data["status"] = Choices.UNAVAILABLE
                validated_data["acquired_by"] = User.objects.get(
                    id=self.initial_data["user_id"]
                )
            elif self.context["request"].query_params.get("action") == "release":
                validated_data["status"] = Choices.AVAILABLE
                validated_data["acquired_by"] = None
        return super().update(instance, validated_data)

    def create(self, validated_data):
        validated_data["organization"] = self.context[
            "request"
        ].user.employee.organization
        return super().create(validated_data)

    def to_internal_value(self, data):
        data = super().to_internal_value(data)
        if "description" in data:
            data["description"] = markdown(data["description"])
        return data
