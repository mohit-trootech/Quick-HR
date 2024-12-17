# Generated by Django 5.1.2 on 2024-12-17 07:22

import django_extensions.db.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("project", "0002_alter_project_assigned_users_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="slug",
            field=django_extensions.db.fields.AutoSlugField(
                blank=True, editable=False, populate_from="title", verbose_name="slug"
            ),
        ),
        migrations.AddField(
            model_name="task",
            name="slug",
            field=django_extensions.db.fields.AutoSlugField(
                blank=True, editable=False, populate_from="title", verbose_name="slug"
            ),
        ),
    ]
