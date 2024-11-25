from django.contrib.admin import register, ModelAdmin
from utils.utils import get_model

Device = get_model(app_name="device", model_name="Device")


@register(Device)
class DeviceAdmin(ModelAdmin):
    list_display = ("title", "status", "acquired_by", "created")
    list_filter = ("status", "acquired_by", "created")
    search_fields = ("title", "description")
    readonly_fields = ("created", "modified")
    ordering = ("-created",)
