from rest_framework.viewsets import ModelViewSet
from quick_hr.api.serializers import BroadCastSerializer, HolidaySerializer
from utils.utils import get_model

BroadCast = get_model(app_name="quick_hr", model_name="BroadCast")
Holiday = get_model(app_name="quick_hr", model_name="Holiday")


class BroadCastView(ModelViewSet):
    queryset = BroadCast.objects.all()
    serializer_class = BroadCastSerializer


class HolidayView(ModelViewSet):
    queryset = Holiday.objects.all()
    serializer_class = HolidaySerializer
    search_fields = ["title", "description"]
    filterset_fields = ["status"]
