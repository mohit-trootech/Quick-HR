from leave.api.api import LeaveViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register("", LeaveViewSet, basename="leave")


urlpatterns = router.urls