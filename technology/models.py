# Create your models here.
from django.db import models
from django_extensions.db.models import TimeStampedModel
from technology.constants import Choices


class Technology(TimeStampedModel):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    status = models.CharField(
        max_length=50, choices=Choices.CHOICES, default=Choices.ACTIVE
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Technology"
        verbose_name_plural = "Technologies"
        ordering = ["-created"]
