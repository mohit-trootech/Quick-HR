from django.contrib.admin import register, ModelAdmin
from utils.utils import get_model


Attendence = get_model(app_name="attendence", model_name="Attendence")


@register(Attendence)
class AttendenceAdmin(ModelAdmin):
    list_display = ["user", "date", "created"]
    list_filter = ["user", "date"]
    search_fields = ["user__username", "date"]
    ordering = ["-date"]
    readonly_fields = ["created", "modified"]
