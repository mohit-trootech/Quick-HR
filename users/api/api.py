from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.mixins import (
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
)
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from utils.utils import get_model
from users.api.serializers import (
    RegistrationSerializer,
    LoginSerializer,
    DetailedUserSerializer,
    ForgotPasswordSerializer,
    OtpVerificationSerializer,
    OrganizationRegisterSerializer,
    OrganizationLoginSerializer,
    LoggedInUserSerializer,
)
from utils.utils import AuthService
from users.tasks import forgot_password_otp, send_credentials
from users.constants import AuthConstantsMessages, PROJECT_MANAGER
from utils.serailizers import RelatedUserSerializer
from rest_framework.decorators import action

User = get_model(app_name="users", model_name="User")
Employee = get_model(app_name="users", model_name="Employee")


class RegistrationApiView(CreateAPIView):
    """User Registeration API View"""

    serializer_class = RegistrationSerializer
    permission_classes = [permissions.AllowAny]


register_view = RegistrationApiView.as_view()


class LoginApiView(APIView):
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


class UserProfileView(
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    GenericViewSet,
):
    serializer_class = DetailedUserSerializer
    queryset = User.objects.filter(is_active=True)


class ForgotPasswordView(APIView):
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


class OtpVerificationView(APIView):
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


class OrganizationRegisterView(RegistrationApiView):
    serializer_class = OrganizationRegisterSerializer


organization_register_view = OrganizationRegisterView.as_view()


class OrganizationLoginView(LoginApiView):
    serializer_class = OrganizationLoginSerializer


organization_login_view = OrganizationLoginView.as_view()


class AuthUserView(APIView):
    serializer_class = LoggedInUserSerializer

    def get(self, request, *args, **kwargs):
        try:
            employee = Employee.objects.get(user=request.user)
            serializer = self.serializer_class(employee)
            return Response(serializer.data)
        except Employee.DoesNotExist:
            return Response(
                {"message": "Employee not found"}, status=status.HTTP_404_NOT_FOUND
            )


logged_in_user_view = AuthUserView.as_view()


class UserList(ListModelMixin, GenericViewSet):
    serializer_class = RelatedUserSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    search_fields = ["username", "first_name", "last_name", "email"]

    def get_queryset(self):
        return self.queryset.filter(is_active=True)

    @action(detail=False, methods=["get"])
    def project_managers(self, request):
        queryset = self.get_queryset().filter(
            employee__department__name=PROJECT_MANAGER
        )
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
