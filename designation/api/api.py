from rest_framework.viewsets import GenericViewSet
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny
from .serializers import DesignationSerializer
from utils.utils import get_model

Designation = get_model(app_name="designation", model_name="Designation")


class DesignationViewSet(RetrieveUpdateDestroyAPIView, GenericViewSet):
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer
    lookup_field = "name"
    permission_classes = [AllowAny]
