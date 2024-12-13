# Generated by Django 5.1.2 on 2024-12-12 12:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("organization", "0002_customization"),
    ]

    operations = [
        migrations.AddField(
            model_name="customization",
            name="holiday",
            field=models.BooleanField(default=True, verbose_name="Holiday"),
        ),
        migrations.AlterField(
            model_name="customization",
            name="review",
            field=models.BooleanField(default=True, verbose_name="Review"),
        ),
    ]