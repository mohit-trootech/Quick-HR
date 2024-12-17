from rest_framework.serializers import ModelSerializer, SerializerMethodField
from utils.serailizers import RelatedUserSerializer
from utils.serailizers import DynamicFieldsBaseSerializer
from utils.utils import get_model
from rest_framework import serializers

Organization = get_model(app_name="organization", model_name="Organization")
Customization = get_model(app_name="organization", model_name="Customization")
User = get_model(app_name="users", model_name="User")


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

    def validate(self, attrs):
        # leave, review, holiday, project are required fields
        if (
            not attrs.get("leave")
            or not attrs.get("review")
            or not attrs.get("holiday")
        ):
            raise serializers.ValidationError(
                "Leave, Review, Holiday are required fields"
            )
        return super().validate(attrs)

    def update(self, instance, validated_data):
        # If field not in validated_data make it False
        for field in self.fields:
            if field not in validated_data and field != "id":
                # check whether field should not be in validated_data & field should not be id
                validated_data[field] = False
        return super().update(instance, validated_data)


class OrganizationSerializer(DynamicFieldsBaseSerializer, ModelSerializer):
    count = SerializerMethodField("users_count")
    customization = CustomizationSerializer(read_only=True)

    class Meta:
        model = Organization
        fields = ["id", "name", "logo", "count", "customization", "admin"]
        extra_kwargs = {"admin": {"read_only": True}}

    def users_count(self, obj):
        return obj.users.count()

    def create(self, validated_data):
        validated_data["admin"] = self.context["request"].user
        instance = super().create(validated_data)
        self.context["request"].user.organization = instance
        self.context["request"].user.save(update_fields=["organization"])
        return instance


class OrganizationUsersSerializer(RelatedUserSerializer):
    class Meta(RelatedUserSerializer.Meta):
        fields = RelatedUserSerializer.Meta.fields + ["organization"]

    def create(self, validated_data):
        validated_data["organization"] = self.context["request"].user.organization
        return super().create(validated_data)
