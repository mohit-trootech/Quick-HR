# Create your models here.
from django.db import models
from django_extensions.db.models import TimeStampedModel
from resignation.constants import Choices, VerboaseName


class Resignation(TimeStampedModel):
    """Resignation Model"""

    user = models.OneToOneField(
        "users.User", on_delete=models.CASCADE, related_name="resignation"
    )
    reason = models.TextField()
    last_working_day = models.DateField(null=True, blank=True)
    status = models.CharField(
        max_length=50, choices=Choices.CHOICES, default=Choices.PENDING
    )

    def __str__(self):
        return VerboaseName.RESIGNATION_STR.format(username=self.user.username)
