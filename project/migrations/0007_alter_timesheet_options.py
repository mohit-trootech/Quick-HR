# Generated by Django 5.1.2 on 2024-12-17 08:33

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("project", "0006_timesheet"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="timesheet",
            options={
                "ordering": ("-created",),
                "verbose_name": "Timesheet",
                "verbose_name_plural": "Timesheets",
            },
        ),
    ]
