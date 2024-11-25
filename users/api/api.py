from rest_framework import permissions, views, status
from rest_framework.response import Response
from utils.utils import get_model
from users.api.serializers import (
    RegistrationSerializer,
    LoginSerializer,
    UserSerializer,
)
from utils.utils import AuthService
from rest_framework.generics import CreateAPIView

User = get_model("users", "User")


class RegistrationApiView(CreateAPIView):
    """User Registeration API View"""

    serializer_class = RegistrationSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        """Register New User"""
        instance = super().create(request, *args, **kwargs)
        return instance


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
