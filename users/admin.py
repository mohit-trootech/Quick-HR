from django.contrib import admin
from utils.utils import get_model
from django.contrib.auth.admin import UserAdmin

User = get_model(app_name="users", model_name="User")
Employee = get_model(app_name="users", model_name="Employee")
Department = get_model(app_name="users", model_name="Department")


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "is_staff",
        "is_active",
        "is_superuser",
        "is_verified",
        "organization_head",
    )
    list_filter = (
        "is_staff",
        "is_superuser",
        "is_active",
        "is_verified",
        "last_login",
        "date_joined",
        "organization_head",
    )
    readonly_fields = ("id", "last_login", "date_joined", "profile_image")

    fieldsets = (
        (None, {"fields": ("id", "username", "password")}),
        (
            "Personal info",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "email",
                    "age",
                    "address",
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                    "organization_head",
                    "is_verified",
                ),
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
        ("Profile Image", {"fields": ("image", "profile_image")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2"),
            },
        ),
    )
    search_fields = ("username", "first_name", "last_name", "email")
    ordering = ("username",)
    filter_horizontal = (
        "groups",
        "user_permissions",
    )


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "organization",
        "department",
        "designation",
    )
    list_filter = ("designation",)
    search_fields = (
        "user__username",
        "organization__name",
        "department",
        "designation",
    )
    ordering = ("user",)


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    ordering = ("name",)
