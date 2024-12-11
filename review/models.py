from django.db import models
from django_extensions.db.models import (
    TimeStampedModel,
    ActivatorModel,
)
from review.constants import Choices, VerboseNames
from django.utils.timezone import now


def _review_month_year():
    """Return Always 1st Date of Current Month"""

    def get_first_day_of_month(dt):
        return dt.replace(day=1)

    return get_first_day_of_month(now()).date()


class Review(TimeStampedModel, ActivatorModel):
    "User Review Model"

    created = models.DateField(default=_review_month_year)
    reviewer = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name=VerboseNames.REVIEWER
    )
    reviewee = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name=VerboseNames.REVIEWEE
    )
    performance_rating = models.IntegerField(
        choices=Choices.RATING_CHOICES, null=True, blank=True
    )
    performance_comment = models.TextField(null=True, blank=True)
    delivery_rating = models.IntegerField(
        choices=Choices.RATING_CHOICES, null=True, blank=True
    )
    delivery_comment = models.TextField(null=True, blank=True)
    socialization_rating = models.IntegerField(
        choices=Choices.RATING_CHOICES, null=True, blank=True
    )
    socialization_comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.reviewer} reviewed {self.reviewee} on {self.created}"

    class Meta:
        verbose_name = VerboseNames.REVIEW
        verbose_name_plural = VerboseNames.REVIEW_PLURAL
        # Revieww & Created Month and year should be unique
        unique_together = (("reviewer", "reviewee", "created"),)

    @property
    def overall_review(self):
        return "{review:.2f}".format(
            review=(
                self.performance_rating
                + self.delivery_rating
                + self.socialization_rating
            )
            / 3
        )
