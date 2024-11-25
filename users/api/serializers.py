from rest_framework import serializers
from utils.utils import get_model
from django.contrib.auth.password_validation import (
    validate_password as password_strength,
)
from users.constants import UserRegistrationMessages, AuthConstantsMessages
from django.contrib.auth import authenticate
from email_validator import validate_email as email_validation
from email_validator import EmailNotValidError


User = get_model("users", "User")


class RegistrationSerializer(serializers.ModelSerializer):
    """
    A Simple Registration Serilizer for User Signup Process
    """

    confirm_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "password",
            "email",
            "first_name",
            "last_name",
            "confirm_password",
        ]
        extra_kwargs = {
            "password": {"write_only": True, "validators": [password_strength]}
        }

    def validate(self, attrs):
        attrs = super().validate(attrs)
        if attrs["password"] == attrs["confirm_password"]:
            return attrs
        raise serializers.ValidationError(
            {"confirm_password": [UserRegistrationMessages.PASSWORD_DOES_NOT_MATCH]}
        )

    def validate_email(self, value):
        """Validate Email Address"""
        try:
            email_validation(value)
            return value
        except EmailNotValidError as e:
            raise serializers.ValidationError(str(e))

    def create(self, validated_data):
        password = validated_data.pop("confirm_password")
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    """User Login Serializer"""

    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        """Validate User Credentials"""
        login_data = {
            "password": attrs.get("password"),
            "username": attrs.get("username"),
        }
        user = authenticate(**login_data)
        if not user:
            raise serializers.ValidationError(
                {"non_field_errors": [AuthConstantsMessages.INVALID_EMAIL_OR_PASSWORD]}
            )
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "age",
            "address",
            "image",
            "is_verified",
            "last_login",
            "date_joined",
        ]
