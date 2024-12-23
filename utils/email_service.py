"""Mail Services"""

from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from utils.utils import get_model, generate_random_password
from django_extensions.db.models import ActivatorModel
from utils.constants import EmailTemplates
from users.constants import ModelFields

EmailTemplate = get_model("quick_hr", "EmailTemplate")
Otp = get_model("users", "Otp")
User = get_model("users", "User")


class EmailService:
    """Email Service Class to Handle Mail"""

    @staticmethod
    def get_template(email_type: str):
        """Returns Email Template if exists else None"""
        try:
            return EmailTemplate.objects.get(
                status=ActivatorModel.ACTIVE_STATUS, email_type=email_type
            )
        except EmailTemplate.DoesNotExist:
            return None

    @staticmethod
    def get_user_otp(user):
        """Generate Otp for User if already Exist delete and generate a new one"""
        try:
            otp = Otp.objects.get(user=user.id)
            otp.delete()
        except User.DoesNotExist:
            pass
        finally:
            otp = Otp.objects.create(user=user)
            return otp

    @staticmethod
    def send_mail(
        subject: str,
        body: str,
        is_html: bool,
        to_email: list,
        template: str | None = None,
    ):
        """This function will be used to send email using celery task based on email template"""
        sender = settings.EMAIL_HOST_USER
        msg = EmailMultiAlternatives(
            subject=subject, from_email=sender, to=to_email, body=body
        )
        if is_html:
            msg.attach_alternative(template, "text/html")
        msg.send(fail_silently=False)
        return f"Email Send Successfully : Subject: {subject}"

    def registration_mail(self, user, password):
        """Sends a registration email to the specified user."""
        template = self.get_template(email_type=EmailTemplates.REGISTRED_SUCCESSFULLY)
        return self.send_mail(
            template.subject,
            template.body.format(username=user.username, password=password),
            template.is_html,
            [user.email],
            template.template,
        )

    def forgot_password_otp(self, user):
        """
        Sends a Forgot Password OTP to the specified user.
        """
        template = self.get_template(email_type=EmailTemplates.PASSWORD_RESET)
        return self.send_mail(
            template.subject,
            template.body.format(
                otp=self.get_user_otp(user).otp, username=user.username
            ),
            template.is_html,
            [user.email],
            template.template,
        )

    def send_credentails(self, user):
        """Send Credentials to the user"""
        template = self.get_template(email_type=EmailTemplates.PASSWORD_RESET_DONE)
        password = generate_random_password()
        user.set_password(password)
        user.is_verified = ModelFields.INACTIVE_STATUS
        user.save(update_fields=["password", "is_verified"])
        return self.send_mail(
            template.subject,
            template.body.format(username=user.username, password=password),
            template.is_html,
            [user.email],
            template.template,
        )
