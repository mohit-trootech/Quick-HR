"""Leave App Constants"""

from django.utils.translation import gettext_noop as _


class VerboseNames:
    """App: Model Verbose Names"""

    LEAVE = _("Leave")
    LEAVE_PLURAL = _("Leaves")
    AVAILABLE_LEAVE = _("Available Leave")
    AVAILABLE_LEAVES = _("Available Leaves")


class Choices:
    """App: Model Choices"""

    CASUAL_LEAVE = "casual_leave"
    EMERGENCY_LEAVE = "emergency_leave"
    LEAVE_TYPES = (
        (CASUAL_LEAVE, _("Casual Leave")),
        (EMERGENCY_LEAVE, _("Emegency Leave")),
    )
    FULL_DAY = "full_day"
    FIRST_HALF = "first_half"
    SECOND_HALF = "second_half"
    LEAVE_DURATION = (
        (FULL_DAY, _("Full Day")),
        (FIRST_HALF, _("First Half")),
        (SECOND_HALF, _("Second Half")),
    )
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"
    LEAVE_STATUS = (
        (PENDING, _("Pending")),
        (APPROVED, _("Approved")),
        (REJECTED, _("Rejected")),
    )
