from django.db.models.signals import post_save
from django.dispatch import receiver
from utils.utils import get_model

Organization = get_model(app_name="organization", model_name="Organization")
Customization = get_model(app_name="organization", model_name="Customization")


@receiver(post_save, sender=Organization)
def create_organization_customization(sender, instance, created, **kwargs):
    if created:
        Customization.objects.create(organization=instance)
