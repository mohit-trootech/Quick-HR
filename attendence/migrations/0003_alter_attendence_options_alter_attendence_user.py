# Generated by Django 5.1.2 on 2024-11-25 10:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("attendence", "0002_alter_attendence_options_alter_attendence_user"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="attendence",
            options={
                "ordering": ["-date"],
                "verbose_name": "attendence",
                "verbose_name_plural": "attendenes",
            },
        ),
        migrations.AlterField(
            model_name="attendence",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="attendenes",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]