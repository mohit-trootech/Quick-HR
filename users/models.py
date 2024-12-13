from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse_lazy
from users.constants import (
    ModelFields,
    THUMBNAIL_PREVIEW_TAG,
    THUMBNAIL_PREVIEW_HTML,
)
from django.utils.html import format_html
from django_extensions.db.models import TimeStampedModel
from users.constants import VerboseNames, Choices
from django.utils.timezone import timedelta


def _upload_to(self, filename):
    """Upload User Profile Image"""
    return "users/{id}/{filename}".format(id=self.id, filename=filename)


def _generate_otp():
    """Generate Unique Secret Otp"""
    import random
    from string import digits

    def generate_otp():
        return "".join(random.choices(digits, k=6))

    return generate_otp()


class Otp(TimeStampedModel):
    otp = models.CharField(max_length=6, default=_generate_otp)
    user = models.OneToOneField("users.User", on_delete=models.CASCADE)

    def __str__(self):
        return f"OTP for {self.user.username}"

    @property
    def expirytime(self):
        return self.created + timedelta(minutes=5)


class User(AbstractUser):
    """Abstract User Model"""

    image = models.ImageField(
        verbose_name=VerboseNames.PROFILE_IMAGE,
        upload_to=_upload_to,
        blank=True,
        null=True,
    )
    email = models.EmailField(verbose_name=VerboseNames.EMAIL_ADDRESS, unique=True)
    is_verified = models.IntegerField(
        verbose_name=VerboseNames.VERIFICATION_STATUS,
        choices=ModelFields.STATUS_CHOICES,
        default=ModelFields.INACTIVE_STATUS,
    )
    age = models.IntegerField(verbose_name=VerboseNames.AGE, blank=True, null=True)
    address = models.TextField(verbose_name=VerboseNames.ADDRESS, blank=True, null=True)
    organization_head = models.BooleanField(default=False)
    organization = models.ForeignKey(
        "organization.Organization",
        on_delete=models.CASCADE,
        related_name="users",
        blank=True,
        null=True,
    )

    @property
    def profile_image(self):
        """Profile Image Viewer"""
        if self.image:
            return format_html(THUMBNAIL_PREVIEW_TAG.format(img=self.image.url))
        return format_html(THUMBNAIL_PREVIEW_HTML)

    def get_absolute_url(self):
        return reverse_lazy("user:details", kwargs={"username": self.username})

    def __str__(self):
        return self.username


class Employee(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="employee")
    company = models.CharField(max_length=255, choices=Choices.COMPANY_CHOICES)
    department = models.CharField(max_length=255)
    designation = models.CharField(max_length=255, choices=Choices.DESGINATION_CHOICES)
    joining_date = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return "{user}'s Employee's details".format(user=self.user)
