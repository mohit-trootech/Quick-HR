# Generated by Django 5.1.2 on 2025-01-01 09:37

import django_markdown_model.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("leave", "0007_alter_availableleave_casual_leaves_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="leave",
            name="description",
            field=django_markdown_model.fields.MarkDownField(default=1),
            preserve_default=False,
        ),
    ]