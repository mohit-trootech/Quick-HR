# Register your models here.
from django.contrib import admin
from utils.utils import get_model

Technology = get_model(app_name="technology", model_name="Technology")


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "status")
    list_filter = ("status",)
    search_fields = ("name", "description")
    readonly_fields = ("created", "modified")
    ordering = ("-created",)
