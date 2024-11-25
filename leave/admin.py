from django.contrib import admin
from utils.utils import get_model

Leave = get_model(app_name="leave", model_name="Leave")


@admin.register(Leave)
class LeaveAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "user",
        "leave_type",
        "duration",
        "start_date",
        "end_date",
        "status",
        "created",
    )
    list_filter = ("leave_type", "duration", "status", "created")
    search_fields = ("title", "user__username")
    readonly_fields = ("created", "modified")
    ordering = ("-created",)
