from overtime.api.api import OvertimeViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register("", OvertimeViewSet, basename="overtime")
urlpatterns = router.urls
