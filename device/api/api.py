from rest_framework.viewsets import ModelViewSet
from utils.utils import get_model
from device.api.serializers import DeviceSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

Device = get_model(app_name="device", model_name="Device")


class DeviceViewset(ModelViewSet):
    serializer_class = DeviceSerializer
    queryset = Device.objects.all()
    search_fields = ("title", "description")

    def filter_queryset(self, queryset):
        return (
            super()
            .filter_queryset(queryset)
            .filter(
                organization=self.request.user.employee.organization,
            )
        )

    @action(detail=False, methods=["GET"])
    def my_devices(self, request):
        """Devices Acquired by Logged in User"""
        queryset = self.queryset.filter(
            organization=self.request.user.employee.organization,
            acquired_by=request.user,
        )
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
