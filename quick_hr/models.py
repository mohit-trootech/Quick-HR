"""Quick PNR Basic Utilities Models"""

from django.db import models
from django_extensions.db.models import (
    ActivatorModel,
    TimeStampedModel,
    TitleDescriptionModel,
)
from django.utils.translation import gettext_lazy as _
from utils.constants import EmailTemplates
from django.utils.timesince import timesince
from django_markdown_model.fields import MarkDownField


class EmailTemplate(TimeStampedModel, ActivatorModel):
    """model for storing email templates"""

    subject = models.CharField(max_length=255, verbose_name=_("subject"))
    body = models.TextField(verbose_name=_("body"))
    template = models.TextField(null=True, blank=True)
    is_html = models.BooleanField(null=True, blank=True)
    email_type = models.CharField(
        max_length=50, choices=EmailTemplates.EMAIL_TYPES, null=True, blank=True
    )

    def __str__(self) -> str:
        """
        Returns a string representation of the model.
        Returns:
            str: The subject of the email template.
        """
        return self.subject


class BroadCast(TitleDescriptionModel, TimeStampedModel, ActivatorModel):
    description = MarkDownField()
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="broadcasts"
    )

    def __str__(self):
        return "BroadCast - {}".format(self.title)

    class Meta:
        verbose_name = _("BroadCast")
        verbose_name_plural = _("BroadCasts")
        ordering = ["-created"]
        unique_together = ["title", "user"]

    @property
    def created_ago(self):
        return timesince(self.created)


class Holiday(TimeStampedModel, TitleDescriptionModel):
    description = MarkDownField()
    starts_from = models.DateField(verbose_name=_("Starts From"))
    ends_on = models.DateField(verbose_name=_("Ends On"))

    class Meta:
        verbose_name = _("Holiday")
        verbose_name_plural = _("Holidays")
        ordering = ["-created"]

    def __str__(self):
        return self.title

    @property
    def no_of_days(self):
        return (self.ends_on - self.starts_from).days + 1
