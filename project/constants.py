"""Project App Constants"""

from django.utils.translation import gettext_noop as _


class VerboseNames:
    """App: Model Verbose Names"""

    PROJECT = _("Project")
    PROJECT_PLURAL = _("Projects")
    PROJECT_MANAGER = "project_manager"
    TEAM_LEAD = "team_lead"
    ASSIGNED_USERS = "assigned_users"

    TASK = _("Task")
    TASK_PLURAL = _("Tasks")


class Choices:
    """App: Model Choices"""

    OPEN = "open"
    IN_PROGRESS = "progress"
    COMPLETE = "complete"
    STATUS = (
        ("open", _("Open")),
        ("progress", _("Progress")),
        ("complete", _("Complete")),
    )
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    PRIORITY = (
        (HIGH, _("High")),
        (MEDIUM, _("Medium")),
        (LOW, _("Low")),
    )
