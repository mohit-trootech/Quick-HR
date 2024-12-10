# Generated by Django 5.1.2 on 2024-12-09 08:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("leave", "0003_availableleave_encashment_leaves_and_more"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="availableleave",
            unique_together=set(),
        ),
        migrations.AddField(
            model_name="availableleave",
            name="casual_leaves",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="availableleave",
            name="emergency_leaves",
            field=models.IntegerField(default=0),
        ),
        migrations.RemoveField(
            model_name="availableleave",
            name="leave_type",
        ),
    ]
