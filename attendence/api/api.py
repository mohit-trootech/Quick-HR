from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet
from attendence.api.serializers import AttendenceSerializer
from utils.utils import get_model

Attendence = get_model(app_name="attendence", model_name="Attendence")


class AttendenceViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    serializer_class = AttendenceSerializer
    queryset = Attendence.objects.all()


attendence_viewset = AttendenceViewSet
