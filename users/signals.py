"""Signals to handle User model related tasks"""

from utils.utils import get_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from utils.user_created_services import AuthUserCreatedServices

User = get_model(app_name="users", model_name="User")


@receiver(post_save, sender=User)
def send_registration_mail(sender, instance, created, **kwargs):
    """Send Registration Mail When User Created"""
    if created:
        auth_user_services = AuthUserCreatedServices(instance)
        auth_user_services.create_user_leaves()
        if not instance.organization_head:
            # If Registered User is Not Organization Head
            password = auth_user_services._generate_password()
            auth_user_services.send_registration_mail(password=password)
            return True
    return False
