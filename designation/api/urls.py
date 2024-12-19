from rest_framework.routers import SimpleRouter
from designation.api.api import DesignationViewSet


router = SimpleRouter()
router.register("designation", DesignationViewSet, basename="designation")
