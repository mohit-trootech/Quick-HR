from django.db.models.signals import post_save
from django.dispatch import receiver
from leave.models import AvailableLeave, Leave
from leave.constants import Choices
from django.db.models import F
from django.utils.timezone import timedelta


@receiver(post_save, sender=Leave)
def update_available_leaves(sender, instance, created, **kwargs):
    """
    Django Signals to automate update process of available leaves based on leave approval
    if leave updated & choice is approved update user's available leave data based on leave types
    & leave duration
    """
    if not created and instance.status == Choices.APPROVED:
        if instance.duration == Choices.FULL_DAY:
            total_days = (instance.end_date - instance.start_date).days + 1
        else:
            total_days = 0.5

        # Check for sandwich leave
        total_days += calculate_sandwich_days(instance.start_date, instance.end_date)

        available_leave = AvailableLeave.objects.get(user=instance.user)
        if instance.leave_type == Choices.CASUAL_LEAVE:
            available_leave.casual_leaves = F("casual_leaves") - total_days
            available_leave.save(update_fields=["casual_leaves"])
        elif instance.leave_type == Choices.EMERGENCY_LEAVE:
            available_leave.emergency_leaves = F("emergency_leaves") - total_days
            available_leave.save(update_fields=["emergency_leaves"])


def calculate_sandwich_days(start_date, end_date):
    """
    Calculate the number of sandwich days (weekends) within the leave period
    """
    sandwich_days = 0
    current_date = start_date

    while current_date <= end_date:
        if current_date.weekday() in (5, 6):
            sandwich_days += 1
        current_date += timedelta(days=1)

    return sandwich_days
