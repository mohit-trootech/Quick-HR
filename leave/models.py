from django.db import models
from django_extensions.db.models import TimeStampedModel, TitleDescriptionModel
from leave.constants import Choices, VerboseNames


class Leave(TimeStampedModel, TitleDescriptionModel):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    leave_type = models.CharField(
        max_length=50, choices=Choices.LEAVE_TYPES, default=Choices.CASUAL_LEAVE
    )
    duration = models.CharField(
        max_length=50, choices=Choices.LEAVE_DURATION, default=Choices.FULL_DAY
    )
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    status = models.CharField(
        max_length=50, choices=Choices.LEAVE_STATUS, default=Choices.PENDING
    )

    class Meta:
        verbose_name = VerboseNames.LEAVE
        verbose_name_plural = VerboseNames.LEAVE_PLURAL

    def __str__(self):
        return f"{self.user.username} - {self.title}"
