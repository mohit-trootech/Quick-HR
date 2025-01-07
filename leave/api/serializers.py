from utils.utils import get_model
from utils.serailizers import DynamicFieldsBaseSerializer, RelatedUserSerializer
from rest_framework.serializers import (
    ModelSerializer,
    ValidationError,
    Serializer,
    DateField,
    CharField,
)
from leave.constants import Choices, AuthMessages


Leave = get_model(app_name="leave", model_name="Leave")
AvailableLeave = get_model(app_name="leave", model_name="AvailableLeave")


class AvailableLeaveSerializer(DynamicFieldsBaseSerializer, ModelSerializer):
    class Meta:
        model = AvailableLeave
        fields = [
            "id",
            "created",
            "modified",
            "emergency_leaves",
            "casual_leaves",
            "encashment_leaves",
            "pending_leaves",
        ]


class LeaveDateValidationSerializer(Serializer):
    """Leave date validation serializer handles the validations of dates and duration"""

    start_date = DateField(required=True)
    end_date = DateField(required=True)
    duration = CharField(max_length=50, required=True)

    def validate(self, attrs):
        if attrs["start_date"] > attrs["end_date"]:
            raise ValidationError(
                {"end_date": [AuthMessages.END_DATE_GREATER_THAN_START_DATE]}
            )
        if (
            attrs["duration"] != Choices.FULL_DAY
            and attrs["start_date"] != attrs["end_date"]
        ):
            raise ValidationError(
                {"non_field_errors": [AuthMessages.HALF_DAY_LEAVE_ERROR]}
            )
        return super().validate(attrs)


class LeaveSerializer(DynamicFieldsBaseSerializer, ModelSerializer):
    user = RelatedUserSerializer(read_only=True)

    class Meta:
        model = Leave
        fields = (
            "id",
            "title",
            "description",
            "start_date",
            "end_date",
            "status",
            "user",
            "leave_type",
            "created",
            "modified",
            "leave_duration",
            "duration",
        )
        read_only_fields = ("id", "created", "modified")
        depth = True

    def validate(self, attrs):
        serializer = LeaveDateValidationSerializer(**attrs)
        serializer.is_valid(raise_exception=True)
        return super().validate(attrs)

    def create(self, validated_data):
        validated_data["user"] = self.context["request"].user
        return super().create(validated_data)
