# Generated by Django 5.1.2 on 2025-01-02 07:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("quick_hr", "0006_alter_emailtemplate_email_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="emailtemplate",
            name="email_type",
            field=models.CharField(
                blank=True,
                choices=[
                    ("verify_email", "Verify Email"),
                    ("registered", "Registered Successfully"),
                    ("password_reset_done", "Password Reset Done"),
                    ("otp_request", "OTP Request"),
                    ("forgot_password_success", "Forgot Password Success"),
                ],
                max_length=50,
                null=True,
            ),
        ),
    ]