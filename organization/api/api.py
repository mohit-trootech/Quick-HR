from rest_framework import viewsets
from organization.api.serializers import OrganizationSerializer
from utils.utils import get_model

Organization = get_model(app_name="organization", model_name="Organization")


class OrganizationView(viewsets.ModelViewSet):
    serializer_class = OrganizationSerializer
    queryset = Organization.objects.all()
    search_fields = ("name",)
    filter_fields = ("name",)
