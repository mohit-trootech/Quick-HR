from leave.api.api import LeaveViewSet, AvailableLeaveViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register("list", LeaveViewSet, basename="leaves-taken")
router.register("available/", AvailableLeaveViewSet, basename="available-leaves")

urlpatterns = router.urls
