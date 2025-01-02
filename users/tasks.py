from celery import shared_task
from utils.email_service import EmailService
from utils.utils import get_model

User = get_model("users", "User")


@shared_task
def registration_mail(id: int, password: str):
    """Sends a registration email to the user."""

    return EmailService().registration_mail(User.objects.get(id=id), password)


@shared_task
def send_otp(email: str):
    """Sends a Forgot Password OTP to the user"""
    return EmailService().send_otp(User.objects.get(email=email))


@shared_task
def account_verification(email: str):
    """Send Account Verification Email to the user"""
    return EmailService().account_verification(User.objects.get(email=email))


@shared_task
def password_reset_done(email: str):
    """Send Password Reset Email to the user"""
    return EmailService().password_reset_done(User.objects.get(email=email))


@shared_task
def send_credentials(email: str):
    """Send Credentials to the user"""
    return EmailService().send_credentails(User.objects.get(email=email))
