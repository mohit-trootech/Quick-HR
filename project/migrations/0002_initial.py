# Generated by Django 5.1.2 on 2024-11-25 16:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("project", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="assigned_users",
            field=models.ManyToManyField(
                blank=True, related_name="assigned_users", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="project",
            name="project_manager",
            field=models.ManyToManyField(
                blank=True, related_name="project_manager", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="project",
            name="team_lead",
            field=models.ManyToManyField(
                blank=True, related_name="team_lead", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="task",
            name="assigned_user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="task",
            name="project",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="project.project"
            ),
        ),
    ]
