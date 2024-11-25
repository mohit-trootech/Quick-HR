from django.contrib.admin import ModelAdmin, register
from utils.utils import get_model

Overtime = get_model(app_name="overtime", model_name="Overtime")


@register(Overtime)
class OvertimeAdmin(ModelAdmin):
    list_display = ("title", "user", "project", "start_time", "end_time", "status")
    list_filter = ("status", "user", "project", "start_time", "end_time")
    search_fields = ("title", "description")
    readonly_fields = ("created", "modified")
    ordering = ("-created",)
    raw_id_fields = ("user", "project")
