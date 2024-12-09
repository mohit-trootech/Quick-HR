from leave.api.api import LeaveViewSet, AvailableLeaveViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register("available", AvailableLeaveViewSet, basename="available-leaves")
router.register("list", LeaveViewSet, basename="leaves-taken")


urlpatterns = router.urls
