"""Users Urls"""

from users.api.api import (
    RegistrationApiView,
    LoginApiView,
    UserProfileView,
)
from django.urls import path, include
from rest_framework.routers import SimpleRouter

router = SimpleRouter()

urlpatterns = [
    path("", include(router.urls)),
    path("login/", RegistrationApiView.as_view(), name="register"),
    path("login/", LoginApiView.as_view(), name="login"),
    path("profile/", UserProfileView.as_view(), name="profile"),
]
