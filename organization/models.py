from django.db import models


def _upload_organization_logo(self, filename):
    return "organizations/logos/{id}/{filename}".format(id=self.id, filename=filename)


class Organization(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to=_upload_organization_logo, blank=True, null=True)
    admin = models.OneToOneField(
        "users.User", on_delete=models.CASCADE, related_name="organization_admin"
    )

    def __str__(self):
        return self.name


class Customization(models.Model):
    organization = models.OneToOneField(
        "organization.Organization",
        on_delete=models.CASCADE,
        related_name="customization",
    )
    leave = models.BooleanField(verbose_name="Leave", default=True)
    overtime = models.BooleanField(verbose_name="Overtime", default=True)
    project = models.BooleanField(verbose_name="Project", default=False)
    review = models.BooleanField(verbose_name="Review", default=True)
    attendence = models.BooleanField(verbose_name="Attendence", default=False)
    salary = models.BooleanField(verbose_name="Salary", default=False)
    device = models.BooleanField(verbose_name="Device", default=False)
    holiday = models.BooleanField(verbose_name="Holiday", default=True)

    def __str__(self):
        return f"{self.organization.name} Customization"
