from django.contrib.admin import ModelAdmin, register
from utils.utils import get_model

Project = get_model(app_name="project", model_name="Project")
Task = get_model(app_name="project", model_name="Task")
Activity = get_model(app_name="project", model_name="Activity")


@register(Project)
class ProjectAdmin(ModelAdmin):
    list_display = ("title", "status", "created")
    list_filter = ("status", "created")
    search_fields = ("title", "description")
    readonly_fields = ("created", "modified")
    ordering = ("-created",)
    filter_horizontal = ("assigned_users",)


@register(Task)
class TaskAdmin(ModelAdmin):
    list_display = (
        "title",
        "project",
        "status",
        "priority",
        "created",
    )
    list_filter = ("status", "priority", "project", "created")
    search_fields = ("title", "description")
    readonly_fields = ("created", "modified")
    ordering = ("-created",)


@register(Activity)
class ActivityAdmin(ModelAdmin):
    list_display = (
        "project",
        "task",
        "user",
        "activity_type",
        "created",
    )
    list_filter = ("activity_type", "created")
    search_fields = ("activity_type",)
    readonly_fields = ("created", "modified")
    ordering = ("-created",)
