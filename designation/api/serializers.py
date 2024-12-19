from utils.utils import get_model
from rest_framework.serializers import ModelSerializer

Designation = get_model(app_name="designation", model_name="Designation")


class DesignationSerializer(ModelSerializer):
    class Meta:
        model = Designation
        fields = ("id", "name")
