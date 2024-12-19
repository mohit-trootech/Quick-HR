from django.contrib import admin
from utils.utils import get_model

Desgination = get_model(app_name="designation", model_name="Designation")


@admin.register(Desgination)
class DesginationAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")
    search_fields = ("name",)
    list_per_page = 25
    ordering = ("name",)
