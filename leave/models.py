from django.db import models
from django_extensions.db.models import TimeStampedModel, TitleDescriptionModel
from leave.constants import Choices, VerboseNames
from django_markdown_model.fields import MarkDownField


class AvailableLeave(TimeStampedModel):
    user = models.OneToOneField(
        "users.User", on_delete=models.CASCADE, related_name="available_leave"
    )
    emergency_leaves = models.DecimalField(default=0.0, decimal_places=1, max_digits=3)
    casual_leaves = models.DecimalField(default=0.0, decimal_places=1, max_digits=3)
    encashment_leaves = models.DecimalField(default=0.0, decimal_places=1, max_digits=3)

    class Meta:
        verbose_name = VerboseNames.AVAILABLE_LEAVE
        verbose_name_plural = VerboseNames.AVAILABLE_LEAVES

    def __str__(self):
        return "{username}'s Available Leaves".format(
            username=self.user.username.capitalize()
        )

    @property
    def pending_leaves(self):
        return self.user.leaves.filter(status=Choices.PENDING).count()


class Leave(TimeStampedModel, TitleDescriptionModel):
    description = MarkDownField()
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="leaves"
    )
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
        ordering = ["-created"]

    def __str__(self):
        return f"{self.user.username} - {self.title}"

    @property
    def leave_duration(self):
        return (self.end_date - self.start_date).days + 1
