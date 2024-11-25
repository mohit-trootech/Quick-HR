"""Overtime App Constants"""

from django.utils.translation import gettext_noop as _


class Choices:
    """App Model Choices"""

    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"
    APPROVAL_STATUS = (
        (PENDING, _("Pending")),
        (APPROVED, _("Approved")),
        (REJECTED, _("Rejected")),
    )


class VerboseNames:
    """App Model Verbose Names"""

    START_TIME = _("Start Time")
    END_TIME = _("End Time")
    OVERTIME = _("Overtime")
    OVERTIME_PLURAL = _("Overtimes")
