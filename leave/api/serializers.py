from utils.utils import get_model
from utils.serailizers import DynamicFieldsBaseSerializer, RelatedUserSerializer
from rest_framework.serializers import ModelSerializer

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
            "available_leaves",
            "encashment_leaves",
            "pending_leaves",
        ]


class LeaveSerializer(DynamicFieldsBaseSerializer):
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
        )
        read_only_fields = ("id", "created", "modified")
        depth = True
