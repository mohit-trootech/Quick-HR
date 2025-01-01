from rest_framework import generics
from organization.api.serializers import (
    OrganizationSerializer,
    CustomizationSerializer,
    OrganizationUsersSerializer,
    DepartmentSerializer,
)
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from utils.utils import get_model

Organization = get_model(app_name="organization", model_name="Organization")
Customization = get_model(app_name="organization", model_name="Customization")
User = get_model(app_name="users", model_name="User")
Department = get_model(app_name="users", model_name="Department")
Employee = get_model(app_name="users", model_name="Employee")


class OrganizationView(ModelViewSet):
    serializer_class = OrganizationSerializer
    queryset = Organization.objects.all()
    search_fields = ("name",)
    filter_fields = ("name",)


class CustomizationView(generics.UpdateAPIView):
    serializer_class = CustomizationSerializer
    queryset = Customization.objects.all()


customization_view = CustomizationView.as_view()


class OrganizationUsersView(generics.ListCreateAPIView):
    serializer_class = OrganizationUsersSerializer
    search_fields = ("username",)
    filter_fields = ("username",)

    def get_queryset(self):
        return Employee.objects.filter(
            organization=self.request.user.organization_admin,
            user__organization_head=False,
        )


organization_users_view = OrganizationUsersView.as_view()


class DepartmentView(generics.ListCreateAPIView, GenericViewSet):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()
    pagination_class = None
