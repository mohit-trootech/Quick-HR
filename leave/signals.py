# When Leave is Created Simply Update Available Leaves Data Based on Leave Type

from django.db.models.signals import post_save
from django.dispatch import receiver
from leave.models import AvailableLeave, Leave
from leave.constants import Choices
from django.db.models import F


@receiver(post_save, sender=Leave)
def update_available_leaves(sender, instance, created, **kwargs):
    total_days = instance.end_date - instance.start_date
    if created:
        available_leave = AvailableLeave.objects.get(user=instance.user)
        if instance.leave_type == Choices.CASUAL_LEAVE:
            available_leave.casual_leaves = F("casual_leaves") + total_days.days
            available_leave.save(update_fields=["casual_leaves"])
        elif instance.leave_type == Choices.EMERGENCY_LEAVE:
            available_leave.emergency_leaves = F("emergency_leaves") + total_days.days
            available_leave.save(update_fields=["emergency_leaves"])
