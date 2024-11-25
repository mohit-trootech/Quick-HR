from review.api.api import ReviewViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()

router.register("reviews", ReviewViewSet, basename="reviews")

urlpatterns = router.urls
