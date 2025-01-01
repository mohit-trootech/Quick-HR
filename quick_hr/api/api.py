from rest_framework.viewsets import ModelViewSet
from quick_hr.api.serializers import (
    BroadCastSerializer,
    HolidaySerializer,
    HolidayCsvSerializer,
)
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from rest_framework.decorators import action
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

    @action(detail=False, methods=["post"])
    def holidays_csv_upload(self, request):
        serializer = HolidayCsvSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response("Holidays created successfully", status=HTTP_201_CREATED)
