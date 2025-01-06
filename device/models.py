from django.db import models
from django_extensions.db.models import TimeStampedModel, TitleSlugDescriptionModel
from device.constants import Choices, VerboseNames
from django_markdown_model.fields import MarkDownField


class Device(TitleSlugDescriptionModel, TimeStampedModel):
    organization = models.ForeignKey(
        "organization.Organization",
        on_delete=models.CASCADE,
        related_name="devices",
    )
    description = MarkDownField()
    status = models.CharField(
        default=True, choices=Choices.STATUS_CHOICES, max_length=16
    )
    acquired_by = models.ForeignKey(
        "users.User",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = VerboseNames.DEVICE
        verbose_name_plural = VerboseNames.DEVICES
        unique_together = ["title", "organization"]

    def __str__(self):
        return self.title
