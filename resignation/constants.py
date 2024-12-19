# Resignation App Constants
from django.utils.translation import gettext_noop as _


class VerboaseName:
    """Resignation Model Verboase Name"""

    RESIGNATION_STR = "{username}'s Resignation"


class Choices:
    """Regisnation Model Choices"""

    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"

    CHOICES = (
        (PENDING, _("Pending")),
        (APPROVED, _("Approved")),
        (REJECTED, _("Rejected")),
    )
