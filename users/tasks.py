from celery import shared_task
from utils.email_service import EmailService
from utils.utils import get_model

User = get_model("users", "User")


@shared_task
def registration_mail(id: int, password: str):
    """Sends a registration email to the user."""

    return EmailService().registration_mail(User.objects.get(id=id), password)


@shared_task
def forgot_password_otp(id: int):
    """Sends a Forgot Password OTP to the user"""
    return EmailService().forgot_password_otp(User.objects.get(id=id))


@shared_task
def send_credentials(email: str):
    """Send Credentials to the user"""
    return EmailService().send_credentails(User.objects.get(email=email))
