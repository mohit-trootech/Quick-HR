# Generated by Django 5.1.2 on 2024-12-11 07:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("review", "0004_remove_review_date_alter_review_created"),
    ]

    operations = [
        migrations.AlterField(
            model_name="review",
            name="delivery_rating",
            field=models.IntegerField(
                blank=True,
                choices=[
                    (0, "Terrible"),
                    (1, "Poor"),
                    (2, "Below Average"),
                    (3, "Average"),
                    (4, "Good"),
                    (5, "Excellent"),
                ],
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="review",
            name="performance_rating",
            field=models.IntegerField(
                blank=True,
                choices=[
                    (0, "Terrible"),
                    (1, "Poor"),
                    (2, "Below Average"),
                    (3, "Average"),
                    (4, "Good"),
                    (5, "Excellent"),
                ],
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="review",
            name="socialization_rating",
            field=models.IntegerField(
                blank=True,
                choices=[
                    (0, "Terrible"),
                    (1, "Poor"),
                    (2, "Below Average"),
                    (3, "Average"),
                    (4, "Good"),
                    (5, "Excellent"),
                ],
                null=True,
            ),
        ),
    ]