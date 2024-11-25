from rest_framework.viewsets import ModelViewSet
from utils.utils import get_model
from device.api.serializers import DeviceSerializer

Device = get_model(app_name="device", model_name="Device")


class DeviceViewset(ModelViewSet):
    serializer_class = DeviceSerializer
    queryset = Device.objects.all()
