from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.utils.timezone import now
from attendence.constants import VerboseNames


def attendence_data(self):
    return now().date()


class Attendence(TimeStampedModel):
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name=VerboseNames.ATTENDENCEES
    )
    date = models.DateField(default=attendence_data)

    class Meta:
        verbose_name = VerboseNames.ATTENDENCE
        verbose_name_plural = VerboseNames.ATTENDENCEES
        ordering = ["-date"]

    def __str__(self):
        return f"{self.user} - {self.date}"
