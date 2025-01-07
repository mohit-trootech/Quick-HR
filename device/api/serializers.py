from rest_framework.serializers import (
    ModelSerializer,
    ValidationError,
    Serializer,
    IntegerField,
    CharField,
)
from utils.serailizers import DynamicFieldsBaseSerializer, RelatedUserSerializer
from utils.utils import get_model
from markdown import markdown
from device.constants import Choices, AuthMessages

Device = get_model(app_name="device", model_name="Device")
User = get_model(app_name="users", model_name="User")


class DeviceAcquireSerializer(Serializer):
    """Device acquire serializer to handle the acquire and release actions"""

    user_id = IntegerField(required=True)
    action = CharField(required=True)

    def validate_user_id(self, value):
        """Validate user id raise error when user not found & action is unauthorized"""
        try:
            user = User.objects.get(id=value)
            if user != self.context["request"].user:
                raise ValidationError(AuthMessages.UNAUTHORIZED_ACTION)
            return value
        except User.DoesNotExist:
            raise ValidationError(AuthMessages.USER_NOT_FOUND)

    def update(self, instance, validated_data):
        """Update the instance based on the action provided."""
        if validated_data["action"] == "acquire":
            if instance.acquired_by:
                raise ValidationError(AuthMessages.ALREADY_ACQUIRED)
            instance.status = Choices.UNAVAILABLE
            instance.acquired_by = User.objects.get(id=validated_data["user_id"])
        elif validated_data["action"] == "release":
            if not instance.acquired_by:
                raise ValidationError(AuthMessages.NOT_ACQUIRED)
            if instance.acquired_by != User.objects.get(id=validated_data["user_id"]):
                raise ValidationError(AuthMessages.UNAUTHORIZED_ACTION)
            instance.status = Choices.AVAILABLE
            instance.acquired_by = None
        return instance


class DeviceSerializer(DynamicFieldsBaseSerializer, ModelSerializer):
    acquired_by = RelatedUserSerializer()

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
            serializer = DeviceAcquireSerializer(
                instance=instance,
                data={
                    "user_id": self.initial_data["user_id"],
                    "action": self.context["request"].query_params["action"],
                },
                context=self.context,
            )
            serializer.is_valid(raise_exception=True)
            instance = serializer.save()
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
