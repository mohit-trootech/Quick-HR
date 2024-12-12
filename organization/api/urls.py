from django.urls import path, include
from rest_framework.routers import SimpleRouter
from organization.api.api import OrganizationView

router = SimpleRouter()
router.register("", OrganizationView, basename="organization")
urlpatterns = [
    path("", include(router.urls)),
]
