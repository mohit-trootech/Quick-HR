from utils.utils import get_model
from rest_framework.serializers import ModelSerializer
from users.api.serializers import BriefUserDetailSerializer

BroadCast = get_model(app_name="quick_hr", model_name="BroadCast")


class BroadCastSerializer(ModelSerializer):
    user = BriefUserDetailSerializer(read_only=True)

    class Meta:
        model = BroadCast
        fields = [
            "id",
            "title",
            "description",
            "user",
            "created_ago",
        ]
        read_only_fields = ["id"]
