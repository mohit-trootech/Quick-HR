from django.db import models
from django_extensions.db.models import TitleDescriptionModel, TimeStampedModel
from overtime.constants import Choices, VerboseNames


class Overtime(TitleDescriptionModel, TimeStampedModel):
    """Overtime Model"""

    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="overtimes"
    )
    project = models.ForeignKey(
        "project.Project", on_delete=models.CASCADE, related_name="overtimes"
    )
    start_time = models.DateTimeField(verbose_name=VerboseNames.START_TIME)
    end_time = models.DateTimeField(verbose_name=VerboseNames.END_TIME)

    status = models.CharField(
        max_length=10,
        choices=Choices.APPROVAL_STATUS,
        default=Choices.PENDING,
    )

    class Meta:
        verbose_name = VerboseNames.OVERTIME
        verbose_name_plural = VerboseNames.OVERTIME_PLURAL

    def __str__(self):
        return self.title
