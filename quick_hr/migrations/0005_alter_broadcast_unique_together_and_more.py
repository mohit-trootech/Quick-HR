# Generated by Django 5.1.2 on 2025-01-01 12:15

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("quick_hr", "0004_alter_broadcast_description_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="broadcast",
            unique_together={("title", "user")},
        ),
        migrations.AlterUniqueTogether(
            name="holiday",
            unique_together={("title", "starts_from", "ends_on")},
        ),
    ]
