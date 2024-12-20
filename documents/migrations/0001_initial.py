# Generated by Django 5.1.2 on 2024-12-19 06:04

import django_extensions.db.fields
import documents.models
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Document",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    django_extensions.db.fields.CreationDateTimeField(
                        auto_now_add=True, verbose_name="created"
                    ),
                ),
                (
                    "modified",
                    django_extensions.db.fields.ModificationDateTimeField(
                        auto_now=True, verbose_name="modified"
                    ),
                ),
                ("title", models.CharField(max_length=255, verbose_name="title")),
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="description"),
                ),
                (
                    "doc",
                    models.FileField(
                        upload_to=documents.models.document_upload_path,
                        verbose_name="Docfile",
                    ),
                ),
            ],
            options={
                "verbose_name": "Document",
                "verbose_name_plural": "Document",
            },
        ),
    ]