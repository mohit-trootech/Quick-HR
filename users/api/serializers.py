from rest_framework import serializers
from utils.utils import get_model
from django.contrib.auth.password_validation import (
    validate_password as password_strength,
)
from users.constants import UserRegistrationMessages, AuthConstantsMessages
from django.contrib.auth import authenticate
from email_validator import validate_email as email_validation
from email_validator import EmailNotValidError
from django.utils.timezone import now
from django.core.exceptions import ObjectDoesNotExist
from utils.serailizers import RelatedUserSerializer

User = get_model(app_name="users", model_name="User")
Otp = get_model(app_name="users", model_name="Otp")
Department = get_model(app_name="users", model_name="Department")
Employee = get_model(app_name="users", model_name="Employee")


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


#  TODO: Create User Profile Page
class DetailedUserSerializer(RelatedUserSerializer):
    class Meta(RelatedUserSerializer.Meta):
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


class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, email):
        """Validate Email"""
        try:
            User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError([AuthConstantsMessages.USE_NOT_FOUND])
        return super().validate(email)


class OtpVerificationSerializer(ForgotPasswordSerializer):
    otp = serializers.CharField()
    email = serializers.EmailField()

    def validate(self, attrs):
        attrs = super().validate(attrs)
        try:
            user = User.objects.get(email=attrs.get("email"))
            if user.otp.otp != attrs["otp"]:
                """Check if OTP is Validated"""
                raise serializers.ValidationError(
                    {"otp": [AuthConstantsMessages.INVALID_OTP]}
                )
            if user.otp.expirytime < now():
                """If Expiry Date if Smaller Than Current Datetime Means OTP is Expired Hence Raise OTP Expiry Validation Error"""
                raise serializers.ValidationError(
                    {"otp": [AuthConstantsMessages.EXPIRED_OTP]}
                )
            return attrs
        except ObjectDoesNotExist as err:
            raise serializers.ValidationError({"non_fields_error": [str(err)]})

    def validate_email(self, email):
        """Validate Email"""
        return super().validate_email(email)


class OrganizationRegisterSerializer(RegistrationSerializer):
    class Meta(RegistrationSerializer.Meta):
        fields = [
            "id",
            "username",
            "password",
            "email",
            "first_name",
            "last_name",
            "confirm_password",
            "organization_head",
            "is_verified",
        ]
        extra_kwargs = {
            "password": {"write_only": True, "validators": [password_strength]},
        }

    def create(self, validated_data):
        """Organization User Registeration Serializer Create Method if User is Organization Head then Set Organization Head to True & Verified to True"""
        validated_data["organization_head"] = True
        validated_data["is_verified"] = True
        return super().create(validated_data)


class OrganizationLoginSerializer(LoginSerializer):
    """Organization Login Serializer"""

    def validate(self, attrs):
        """Validate User Credentials"""
        user = super().validate(attrs)
        if not user.organization_head:
            raise serializers.ValidationError(
                {"non_field_errors": ["You are not authorized to access this page"]}
            )
        return user


class LoggedInUserSerializer(serializers.ModelSerializer):
    user = RelatedUserSerializer()

    class Meta:
        model = Employee
        fields = [
            "id",
            "user",
            "organization",
            "department",
            "designation",
        ]
        read_only_fields = ["id", "user", "organization", "department", "designation"]
        depth = True


class OrganizationLoggedInAdminSerializer(RelatedUserSerializer):

    class Meta(RelatedUserSerializer.Meta):
        fields = RelatedUserSerializer.Meta.fields + [
            "first_name",
            "last_name",
            "last_login",
            "organization_head",
            "organization_admin",
        ]
        depth = 1
