"""Review App Constants"""

from django.utils.translation import gettext_noop as _


class AuthMessages:
    """App: Review Auth Messages"""

    USER_NOT_FOUND = _("User not found.")
    REVIEWER_NOT_FOUND = _("Reviewer not found.")
    REVIEWEE_NOT_FOUND = _("Reviewee not found.")
    REVIEWER_REVIEWEE_SAME = _("Reviewer and reviewee cannot be the same.")
    REVIEWER_REVIEWEE_DIFFERENT_ORGANIZATION = _(
        "Reviewer and reviewee should be in the same organization."
    )
    REVIEWER_REVIEWEE_DIFFERENT_DEPARTMENT = _(
        "Reviewer and reviewee should be in the same department."
    )
    REVIEW_ALREADY_EXISTS = _("Review already exists.")


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
