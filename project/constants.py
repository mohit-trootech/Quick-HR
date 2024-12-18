"""Project App Constants"""

from django.utils.translation import gettext_noop as _


class VerboseNames:
    """App: Model Verbose Names"""

    # Project
    PROJECT = _("Project")
    PROJECT_PLURAL = _("Projects")
    PROJECT_MANAGER = "projects"
    TEAM_LEAD = "team_lead"
    ASSIGNED_USERS = "assigned_users"

    # Task
    TASK = _("Task")
    TASK_PLURAL = _("Tasks")

    # Activity
    ACTIVITY_SINGULAR = _("Activity")
    ACTIVITY_PLURAL = _("Activities")
    ACTIVITY = "activity"


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
    TIMER_START = "start"
    TIMER_STOP = "stop"
    TIMER_PAUSE = "pause"
    TIMER_RESUME = "resume"
    TIMER = (
        (TIMER_START, _("Start")),
        (TIMER_STOP, _("Stop")),
        (TIMER_PAUSE, _("Pause")),
        (TIMER_RESUME, _("Resume")),
    )
