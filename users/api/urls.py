"""Users Urls"""

from users.api.api import (
    register_view,
    login_view,
    otp_request_view,
    otp_verification,
    organization_register_view,
    organization_login_view,
    logged_in_user_view,
    logged_in_admin_view,
    account_verification,
    password_reset_view,
    UserProfileView,
    UserList,
)
from django.urls import path, include
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register("profile", UserProfileView, basename="profile")
router.register("user-list", UserList, basename="user-list")
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
    path("logged-in-admin/", logged_in_admin_view, name="logged-in-admin"),
    path("organization-login/", organization_login_view, name="organization-login"),
    path("otp-request/", otp_request_view, name="otp-request"),
    path("account-verification/", account_verification, name="account-verification"),
    path("otp-verification/", otp_verification, name="otp-verification"),
    path("password-reset/", password_reset_view, name="password-reset"),
]
