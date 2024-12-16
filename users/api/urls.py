"""Users Urls"""

from users.api.api import (
    register_view,
    login_view,
    forgot_password,
    otp_verification,
    organization_register_view,
    organization_login_view,
    logged_in_user_view,
    UserProfileView,
)
from django.urls import path, include
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register("profile", UserProfileView, basename="profile")
urlpatterns = [
    path("", include(router.urls)),
    path("register/", register_view, name="register"),
    path(
        "organization-register/",
        organization_register_view,
        name="organization-register",
    ),
    path("login/", login_view, name="login"),
    path("logged-in-user/", logged_in_user_view, name="logged-in-user"),
    path("organization-login/", organization_login_view, name="organization-login"),
    path("forgot-password/", forgot_password, name="forgot-password"),
    path("otp-verification/", otp_verification, name="otp-verification"),
]
