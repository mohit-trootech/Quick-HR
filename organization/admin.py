from django.contrib import admin
from utils.utils import get_model


Organization = get_model(app_name="organization", model_name="Organization")
Customization = get_model(app_name="organization", model_name="Customization")


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    filter_horizontal = ("users",)


@admin.register(Customization)
class CustomizationAdmin(admin.ModelAdmin):
    list_display = ("organization",)
    search_fields = ("organization__name",)
