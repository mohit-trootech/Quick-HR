from django.contrib.admin import ModelAdmin, register
from utils.utils import get_model

Project = get_model(app_name="project", model_name="Project")
Task = get_model(app_name="project", model_name="Task")


@register(Project)
class ProjectAdmin(ModelAdmin):
    list_display = ("title", "status", "created")
    list_filter = ("status", "created")
    search_fields = ("title", "description")
    readonly_fields = ("created", "modified")
    ordering = ("-created",)
    filter_horizontal = ("project_manager", "team_lead", "assigned_users")


@register(Task)
class TaskAdmin(ModelAdmin):
    list_display = (
        "title",
        "project",
        "assigned_user",
        "status",
        "priority",
        "created",
    )
    list_filter = ("status", "priority", "assigned_user", "project", "created")
    search_fields = ("title", "description")
    readonly_fields = ("created", "modified")
    ordering = ("-created",)
