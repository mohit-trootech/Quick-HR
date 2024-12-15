from rest_framework.serializers import ModelSerializer, SerializerMethodField
from users.api.serializers import BriefUserDetailSerializer
from utils.serailizers import DynamicFieldsBaseSerializer
from utils.utils import get_model

Organization = get_model(app_name="organization", model_name="Organization")
Customization = get_model(app_name="organization", model_name="Customization")


class CustomizationSerializer(ModelSerializer):
    class Meta:
        model = Customization
        fields = [
            "id",
            "leave",
            "overtime",
            "project",
            "review",
            "attendence",
            "salary",
            "device",
            "holiday",
        ]


class OrganizationSerializer(DynamicFieldsBaseSerializer, ModelSerializer):
    count = SerializerMethodField("users_count")
    customization = CustomizationSerializer(read_only=True)

    class Meta:
        model = Organization
        fields = ["id", "name", "logo", "count", "customization"]

    def users_count(self, obj):
        return obj.users.count()

    def create(self, validated_data):
        validated_data["admin"] = self.context["request"].user
        return super().create(validated_data)


class OrganizationUsersSerializer(OrganizationSerializer):
    users = BriefUserDetailSerializer(many=True, read_only=True)

    class Meta(OrganizationSerializer.Meta):
        fields = ["id", "users"]
