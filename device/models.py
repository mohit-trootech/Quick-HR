from django.db import models
from django_extensions.db.models import TimeStampedModel, TitleSlugDescriptionModel
from device.constants import Choices, VerboseNames


class Device(TitleSlugDescriptionModel, TimeStampedModel):
    status = models.CharField(
        default=True, choices=Choices.STATUS_CHOICES, max_length=16
    )
    acquired_by = models.OneToOneField(
        "users.User",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = VerboseNames.DEVICE
        verbose_name_plural = VerboseNames.DEVICES

    def __str__(self):
        return self.title
