from rest_framework import generics
from organization.api.serializers import (
    OrganizationSerializer,
    CustomizationSerializer,
    OrganizationUserCreateSerializer,
)
from utils.utils import get_model

Organization = get_model(app_name="organization", model_name="Organization")
Customization = get_model(app_name="organization", model_name="Customization")
User = get_model(app_name="users", model_name="User")


class OrganizationView(generics.CreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrganizationSerializer
    queryset = Organization.objects.all()
    search_fields = ("name",)
    filter_fields = ("name",)
    lookup_field = "admin__username"
    lookup_url_kwarg = "admin"


organization_view = OrganizationView.as_view()


class CustomizationView(generics.UpdateAPIView):
    serializer_class = CustomizationSerializer
    queryset = Customization.objects.all()

    def get_serializer(self, *args, **kwargs):
        return super().get_serializer(*args, **kwargs)


customization_view = CustomizationView.as_view()


class OrganizationUsersView(generics.ListCreateAPIView):
    serializer_class = OrganizationUserCreateSerializer
    queryset = User.objects.all()
    search_fields = ("username",)
    filter_fields = ("username",)

    def get_queryset(self):
        return self.queryset.filter(organization=self.request.user.organization_admin)


organization_users_view = OrganizationUsersView.as_view()
