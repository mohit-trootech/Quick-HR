from utils.utils import get_model
from rest_framework.serializers import ModelSerializer
from utils.serailizers import DynamicFieldsBaseSerializer, RelatedUserSerializer

Overtime = get_model(app_name="overtime", model_name="Overtime")


class OvertimeSerializer(DynamicFieldsBaseSerializer, ModelSerializer):
    user = RelatedUserSerializer(read_only=True)

    class Meta:
        model = Overtime
        fields = (
            "id",
            "title",
            "description",
            "user",
            "project",
            "start_time",
            "end_time",
            "status",
            "created",
            "modified",
        )
        read_only_fields = ("id", "created", "modified")
        depth = True
