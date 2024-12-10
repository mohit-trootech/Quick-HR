"""Users Urls"""

from users.api.api import (
    register_view,
    login_view,
    profile_view,
    forgot_password,
    otp_verification,
    user_permissions_view,
)
from django.urls import path, include
from rest_framework.routers import SimpleRouter

router = SimpleRouter()

urlpatterns = [
    path("", include(router.urls)),
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("forgot-password/", forgot_password, name="forgot-password"),
    path("otp-verification/", otp_verification, name="otp-verification"),
    path("profile/", profile_view, name="profile"),
    path("user-permissions", user_permissions_view, name="user-permissions"),
]
