# Register your models here.
from django.contrib import admin
from utils.utils import get_model

Resignation = get_model(app_name="resignation", model_name="Resignation")


@admin.register(Resignation)
class ResignationAdmin(admin.ModelAdmin):
    list_display = ("user", "reason", "last_working_day", "status")
    list_filter = ("status",)
    search_fields = ("user__username", "reason")
    readonly_fields = ("created", "modified")
    ordering = ("-created",)
