# Generated by Django 5.1.2 on 2024-12-19 12:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("project", "0015_alter_task_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="activity",
            name="activity_type",
            field=models.CharField(
                choices=[
                    ("start", "Start"),
                    ("stop", "Stop"),
                    ("pause", "Pause"),
                    ("progress", "Progress"),
                ],
                default="start",
                max_length=16,
            ),
        ),
    ]
