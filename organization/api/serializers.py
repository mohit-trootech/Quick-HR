from rest_framework.serializers import ModelSerializer, SerializerMethodField
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
