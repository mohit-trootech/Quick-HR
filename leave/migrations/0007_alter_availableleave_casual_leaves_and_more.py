# Generated by Django 5.1.2 on 2024-12-23 04:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("leave", "0006_alter_leave_options"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="availableleave",
            name="casual_leaves",
            field=models.DecimalField(decimal_places=1, default=0.0, max_digits=3),
        ),
        migrations.AlterField(
            model_name="availableleave",
            name="emergency_leaves",
            field=models.DecimalField(decimal_places=1, default=0.0, max_digits=3),
        ),
        migrations.AlterField(
            model_name="availableleave",
            name="encashment_leaves",
            field=models.DecimalField(decimal_places=1, default=0.0, max_digits=3),
        ),
        migrations.AlterField(
            model_name="availableleave",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="available_leave",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]