from rest_framework import generics
from organization.api.serializers import (
    OrganizationSerializer,
    CustomizationSerializer,
    OrganizationUsersSerializer,
)
from rest_framework.viewsets import ModelViewSet
from utils.utils import get_model

Organization = get_model(app_name="organization", model_name="Organization")
Customization = get_model(app_name="organization", model_name="Customization")
User = get_model(app_name="users", model_name="User")


class OrganizationView(ModelViewSet):
    serializer_class = OrganizationSerializer
    queryset = Organization.objects.all()
    search_fields = ("name",)
    filter_fields = ("name",)
    lookup_field = "admin__username"
    lookup_url_kwarg = "admin"


class CustomizationView(generics.UpdateAPIView):
    serializer_class = CustomizationSerializer
    queryset = Customization.objects.all()


customization_view = CustomizationView.as_view()


class OrganizationUsersView(generics.ListCreateAPIView):
    serializer_class = OrganizationUsersSerializer
    search_fields = ("username",)
    filter_fields = ("username",)

    def get_queryset(self):
        return User.objects.filter(
            organization=self.request.user.organization_admin, organization_head=False
        )


organization_users_view = OrganizationUsersView.as_view()
