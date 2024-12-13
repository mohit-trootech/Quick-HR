from rest_framework import generics
from organization.api.serializers import OrganizationSerializer, CustomizationSerializer
from utils.utils import get_model

Organization = get_model(app_name="organization", model_name="Organization")
Customization = get_model(app_name="organization", model_name="Customization")


class OrganizationView(generics.RetrieveUpdateDestroyAPIView):
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


customization_view = CustomizationView.as_view()
