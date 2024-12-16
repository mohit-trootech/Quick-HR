from django.urls import path
from organization.api.api import (
    customization_view,
    organization_users_view,
    OrganizationView,
)
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register("organizations", OrganizationView, basename="organizations")

urlpatterns = router.urls + [
    path("customization/<int:pk>/", customization_view),
    path("organization-users/", organization_users_view),
]
