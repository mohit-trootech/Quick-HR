# Generated by Django 5.1.2 on 2024-12-12 08:24

import organization.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Organization",
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
                ("name", models.CharField(max_length=255)),
                (
                    "logo",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to=organization.models._upload_organization_logo,
                    ),
                ),
                (
                    "users",
                    models.ManyToManyField(
                        related_name="organizations", to=settings.AUTH_USER_MODEL
                    ),
                ),
            ],
        ),
    ]