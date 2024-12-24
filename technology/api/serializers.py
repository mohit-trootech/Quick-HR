from utils.utils import get_model
from rest_framework.serializers import ModelSerializer

Technology = get_model(app_name="technology", model_name="Technology")


class TechnologySerializer(ModelSerializer):
    class Meta:
        model = Technology
        fields = ["id", "name", "status"]
        extra_kwargs = {"status": {"write_only": True}}
