"""Review App Constants"""

from django.utils.translation import gettext_noop as _


class VerboseNames:
    """App: Model Verbose Names"""

    REVIEW = _("Review")
    REVIEW_PLURAL = _("Reviews")
    REVIEWER = "reviewer"
    REVIEWEE = "reviewee"


class Choices:
    """App: Model Choices"""

    POOR = 1
    BELOW_AVERAGE = 2
    AVERAGE = 3
    GOOD = 4
    EXCELLENT = 5

    RATING_CHOICES = (
        (POOR, _("Poor")),
        (BELOW_AVERAGE, _("Below Average")),
        (AVERAGE, _("Average")),
        (GOOD, _("Good")),
        (EXCELLENT, _("Excellent")),
    )
