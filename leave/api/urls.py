from leave.api.api import LeaveViewSet, available_leave
from rest_framework.routers import SimpleRouter
from django.urls import path

router = SimpleRouter()
router.register("list", LeaveViewSet, basename="leaves-taken")

urlpatterns = router.urls + [
    path("available-leaves/", available_leave),
]
