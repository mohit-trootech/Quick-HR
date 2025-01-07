"""Project App Constants"""

from django.utils.translation import gettext_noop as _


class AuthMessage:
    """App: Project Auth Messages"""

    PROJECT_EXISTS = _("Project already exists.")
    TASK_EXISTS = _("Task already exists")
    PROJECT_IS_REQUIRED = _("Project is required field")
    PROJECT_NOT_EXISTS = _("Project does not exists")
    MULTIPLE_PROJECTS_FOUND = _("Multiple projects found")
    TASK_NOT_EXISTS = _("Task does not exists")
    MULTIPLE_TASKS_FOUND = _("Multiple tasks found")
    ACTIVITY_EXISTS = _("Activity already exists")


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
    TIMER_PROGRESS = "progress"
    TIMER = (
        (TIMER_START, _("Start")),
        (TIMER_STOP, _("Stop")),
        (TIMER_PAUSE, _("Pause")),
        (TIMER_PROGRESS, _("Progress")),
    )
