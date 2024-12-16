from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import AllowAny
from attendence.api.serializers import AttendenceSerializer
from utils.utils import get_model

Attendence = get_model(app_name="attendence", model_name="Attendence")


class AttendenceViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    serializer_class = AttendenceSerializer
    queryset = Attendence.objects.all()
    permissions_classes = [AllowAny]


attendence_viewset = AttendenceViewSet
