# Create your models here.
from django.db import models
from django_extensions.db.models import TimeStampedModel, ActivatorModel
from django_markdown_model.fields import MarkDownField


class Technology(TimeStampedModel, ActivatorModel):
    name = models.CharField(max_length=255, unique=True)
    description = MarkDownField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Technology"
        verbose_name_plural = "Technologies"
        ordering = ["-created"]
