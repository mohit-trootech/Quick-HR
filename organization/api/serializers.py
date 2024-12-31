from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    CurrentUserDefault,
)
from utils.serailizers import RelatedUserSerializer
from utils.serailizers import DynamicFieldsBaseSerializer
from utils.utils import get_model
from rest_framework import serializers

Organization = get_model(app_name="organization", model_name="Organization")
Customization = get_model(app_name="organization", model_name="Customization")
User = get_model(app_name="users", model_name="User")
Employee = get_model(app_name="users", model_name="Employee")
Deparment = get_model(app_name="users", model_name="Department")


class DepartmentSerializer(ModelSerializer):
    class Meta:
        model = Deparment
        fields = ["id", "name"]

    def create(self, validated_data):
        validated_data["organization"] = self.context["request"].user.organization_admin
        return super().create(validated_data)


class CustomizationSerializer(ModelSerializer):
    class Meta:
        model = Customization
        fields = [
            "id",
            "overtime",
            "project",
            "attendence",
            "salary",
            "device",
        ]

    def update(self, instance, validated_data):
        # If field not in validated_data make it False
        for field in self.fields:
            if field not in validated_data and field != "id":
                # check whether field should not be in validated_data & field should not be id
                validated_data[field] = False
        return super().update(instance, validated_data)


class OrganizationSerializer(DynamicFieldsBaseSerializer, ModelSerializer):
    count = SerializerMethodField()
    customization = CustomizationSerializer(read_only=True)
    admin = RelatedUserSerializer(default=CurrentUserDefault())

    class Meta:
        model = Organization
        fields = ["id", "name", "logo", "count", "customization", "admin"]

    def validate_admin(self, value):
        if not value.organization_head:
            raise serializers.ValidationError(
                "Only Organization Head can create Organization"
            )
        return value

    def get_count(self, obj):
        return obj.employees.count()


class OrganizationUsersSerializer(serializers.ModelSerializer):
    user = RelatedUserSerializer()

    class Meta:
        model = Employee
        fields = ["id", "user", "organization", "department", "designation"]
        read_only_fields = ["id", "organization"]

    def create(self, validated_data):
        validated_data["organization"] = self.context["request"].user.organization
        return super().create(validated_data)
