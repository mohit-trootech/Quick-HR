# Generated by Django 5.1.2 on 2024-12-10 10:07

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("leave", "0005_remove_availableleave_available_leaves"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="leave",
            options={
                "ordering": ["-created"],
                "verbose_name": "Leave",
                "verbose_name_plural": "Leaves",
            },
        ),
    ]
