# Generated by Django 5.1.2 on 2025-01-01 09:37

import django_markdown_model.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("documents", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="document",
            name="description",
            field=django_markdown_model.fields.MarkDownField(default=1),
            preserve_default=False,
        ),
    ]
