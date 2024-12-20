from utils.utils import get_model
from rest_framework.serializers import ModelSerializer
from utils.serailizers import RelatedUserSerializer

Resignation = get_model(app_name="resignation", model_name="Resignation")


class ResignationSerializer(ModelSerializer):
    user = RelatedUserSerializer(read_only=True)

    class Meta:
        model = Resignation
        fields = ["id", "user", "reason", "last_working_day", "created", "status"]
