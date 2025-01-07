from rest_framework.viewsets import ModelViewSet
from quick_hr.api.serializers import (
    BroadCastSerializer,
    HolidaySerializer,
    HolidayCsvSerializer,
)
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_200_OK
from rest_framework.decorators import action
from utils.utils import get_model
from quick_hr.constants import AuthMessages
from rest_framework.views import APIView

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
        return Response(AuthMessages.HOLIDAYS_CREATED, status=HTTP_201_CREATED)


class FireStoreConfiguration(APIView):
    """Fire Store DB Configuration"""

    def get(self, request):
        from dotenv import dotenv_values

        config = dotenv_values(".env")
        return Response(
            {
                "apiKey": config["API_KEY"],
                "authDomain": config["AUTH_DOMAIN"],
                "projectId": config["PROJECT_ID"],
                "storageBucket": config["STORAGE_BUCKET"],
                "messagingSenderId": config["MESSAGING_SENDER_ID"],
                "appId": config["APP_ID"],
                "measurementId": config["MEASUREMENT_ID"],
            },
            status=HTTP_200_OK,
        )


firestore_configuration = FireStoreConfiguration.as_view()
