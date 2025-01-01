from utils.utils import get_model
from rest_framework.serializers import ModelSerializer, CurrentUserDefault
from users.api.serializers import RelatedUserSerializer

BroadCast = get_model(app_name="quick_hr", model_name="BroadCast")
Holiday = get_model(app_name="quick_hr", model_name="Holiday")


class BroadCastSerializer(ModelSerializer):
    user = RelatedUserSerializer(default=CurrentUserDefault())

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


class HolidaySerializer(ModelSerializer):
    class Meta:
        model = Holiday
        fields = ["id", "title", "description", "starts_from", "ends_on", "no_of_days"]
        read_only_fields = ["id"]
