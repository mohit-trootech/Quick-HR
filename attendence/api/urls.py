from attendence.api.api import attendence_viewset
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register("", attendence_viewset)

urlpatterns = router.urls
