from utils.utils import get_model
from utils.serailizers import DynamicFieldsBaseSerializer, RelatedUserSerializer

Leave = get_model(app_name="leave", model_name="Leave")


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
