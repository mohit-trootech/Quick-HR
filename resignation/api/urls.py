from resignation.api.api import ResignationViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register("resignation", ResignationViewSet, basename="resignation")
