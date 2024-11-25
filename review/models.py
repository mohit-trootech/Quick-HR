from django.db import models
from django_extensions.db.models import (
    TimeStampedModel,
    ActivatorModel,
)
from review.constants import Choices, VerboseNames


class Review(TimeStampedModel, ActivatorModel):
    "User Review Model"

    month = models.DateField()
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
