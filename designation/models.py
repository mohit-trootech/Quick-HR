from django.db import models
from designation.constants import VerboseNames


class Designation(models.Model):
    name = models.CharField(max_length=64)

    class Meta:
        verbose_name = VerboseNames.TITLE
        verbose_name_plural = VerboseNames.TITLE_PLURAL
        ordering = ["name"]

    def __str__(self):
        return self.name
