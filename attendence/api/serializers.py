from rest_framework.serializers import ModelSerializer
from utils.serailizers import DynamicFieldsBaseSerializer, RelatedUserSerializer
from utils.utils import get_model

Attendence = get_model(app_name="attendence", model_name="Attendence")


class AttendenceSerializer(DynamicFieldsBaseSerializer, ModelSerializer):
    user = RelatedUserSerializer(read_only=True)

    class Meta:
        model = Attendence
        fields = ("id", "user", "date", "created", "modified")
        read_only_fields = ("created", "modified")
        depth = 1
