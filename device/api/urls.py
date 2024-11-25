from device.api.api import DeviceViewset
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register("devices", DeviceViewset, basename="devices")
urlpatterns = router.urls
