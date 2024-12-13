# Generated by Django 5.1.2 on 2024-12-13 06:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("organization", "0004_organization_admins"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name="organization",
            name="admins",
        ),
        migrations.AddField(
            model_name="organization",
            name="admin",
            field=models.OneToOneField(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="organization",
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
    ]
