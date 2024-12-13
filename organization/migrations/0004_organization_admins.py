# Generated by Django 5.1.2 on 2024-12-13 06:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("organization", "0003_customization_holiday_alter_customization_review"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="organization",
            name="admins",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="admin",
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
    ]
