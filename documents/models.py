from django.db import models
from django_extensions.db.models import TimeStampedModel, TitleDescriptionModel

from documents.constants import Constants, VerboseName


def document_upload_path(instance, filename):
    return Constants.DOCUMENT_UPLOAD_PATH.format(
        id=instance.id,
        filename=filename,
    )


class Document(TitleDescriptionModel, TimeStampedModel):
    """Document model to store documents related to various models."""

    doc = models.FileField(
        upload_to=document_upload_path, verbose_name=VerboseName.DOCFILE
    )

    class Meta:
        verbose_name = VerboseName.DOCUMENT
        verbose_name_plural = VerboseName.DOCUMENT

    def __str__(self):
        return f"{self.docfile.name}"
