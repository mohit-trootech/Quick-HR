from utils.utils import get_model
from utils.serailizers import DynamicFieldsBaseSerializer, RelatedUserSerializer
from rest_framework.serializers import (
    ModelSerializer,
    ValidationError,
)
from leave.constants import Choices


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
        """Validate Leave Serializer Data"""
        # Check Whether start_date < end_date
        if attrs["start_date"] > attrs["end_date"]:
            raise ValidationError(
                {"end_date": ["End date must be greater than or equal to start date."]}
            )
        # If Leave Type != Choices.FULL_DAY Then start_day = end_day
        if (
            attrs["duration"] != Choices.FULL_DAY
            and attrs["start_date"] != attrs["end_date"]
        ):
            raise ValidationError(
                {
                    "non_field_errors": [
                        "For half day leave, start date and end date must be same."
                    ]
                }
            )
        return super().validate(attrs)

    def create(self, validated_data):
        validated_data["user"] = self.context["request"].user
        return super().create(validated_data)
