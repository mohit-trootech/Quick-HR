from rest_framework import permissions, views, status, mixins, viewsets
from rest_framework.response import Response
from utils.utils import get_model
from users.api.serializers import (
    RegistrationSerializer,
    LoginSerializer,
    UserSerializer,
    ForgotPasswordSerializer,
    OtpVerificationSerializer,
    BriefUserDetailSerializer,
)
from utils.utils import AuthService
from rest_framework.generics import CreateAPIView
from users.tasks import forgot_password_otp, send_credentials
from users.constants import AuthConstantsMessages


User = get_model("users", "User")


class RegistrationApiView(CreateAPIView):
    """User Registeration API View"""

    serializer_class = RegistrationSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        """Register New User"""
        instance = super().create(request, *args, **kwargs)
        return instance


register_view = RegistrationApiView.as_view()


class LoginApiView(views.APIView):
    """User Login API View"""

    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, *args, **kwargs):
        serializer = self.serializer_class(
            data=self.request.data, context={"request": self.request}
        )
        serializer.is_valid(raise_exception=True)
        return Response(
            AuthService().get_auth_tokens_for_user(serializer.validated_data),
            status=status.HTTP_200_OK,
        )


login_view = LoginApiView.as_view()


class UserProfileView(views.APIView):
    serializer_class = UserSerializer
    queryset = User.objects.filter(is_active=True)
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, *args, **kwargs):
        """Return User Object"""
        return self.request.user

    def get(self, *args, **kwargs):
        """Return User Profile"""
        instance = self.get_object(*args, **kwargs)
        serializer = self.serializer_class(instance)
        return Response(serializer.data)

    def patch(self, request, *args, **kwargs):
        """Update User Profile"""
        instance = self.get_object()
        serializer = self.serializer_class(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


profile_view = UserProfileView.as_view()


class ForgotPasswordView(views.APIView):
    """Forgot Password API View"""

    permission_classes = [permissions.AllowAny]
    serializer_class = ForgotPasswordSerializer

    def post(self, request, *args, **kwargs):
        """Forgot Password"""
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            user = User.objects.get(email=serializer.validated_data.get("email"))
            forgot_password_otp.delay(user.id)
        except User.DoesNotExist:
            return Response(
                {"message": AuthConstantsMessages.USE_NOT_FOUND},
                status=status.HTTP_404_NOT_FOUND,
            )
        return Response(
            {"message": AuthConstantsMessages.EMAIL_VERIFIED_OTP_DELIVERED},
            status=status.HTTP_200_OK,
        )


forgot_password = ForgotPasswordView.as_view()


class OtpVerificationView(views.APIView):
    """OTP Verification API View"""

    serializer_class = OtpVerificationSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        """Verify User Otp"""
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        send_credentials.delay(serializer.validated_data.get("email"))
        return Response({"message": AuthConstantsMessages.CREDENTIALS_SEND_ON_MAIL})


otp_verification = OtpVerificationView.as_view()


class UserPermissionsView(views.APIView):
    """Current Logged In User Permissions"""

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """Return User Permissions"""
        permissions = request.user.get_all_permissions()
        return Response({"permissions": permissions})


user_permissions_view = UserPermissionsView.as_view()


class UserList(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = BriefUserDetailSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    search_fields = ["username", "first_name", "last_name", "email"]

    def get_queryset(self):
        return self.queryset.filter(is_active=True)


user_list = UserList.as_view({"get": "list"})
