# Generated by Django 5.1.2 on 2024-12-19 11:31

import django_markdown_model.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("project", "0014_alter_activity_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="description",
            field=django_markdown_model.fields.MarkDownField(blank=True, null=True),
        ),
    ]