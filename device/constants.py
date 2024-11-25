"""Device App Constants"""

from django.utils.translation import gettext_noop as _


class Choices:
    """App Model Choices"""

    # Status Choice
    AVAILABLE = "available"
    UNAVAILABLE = "unavailable"
    STATUS_CHOICES = (
        (AVAILABLE, _("Available")),
        (UNAVAILABLE, _("Unavailable")),
    )

    #


class VerboseNames:
    """App Model Verbose Names"""

    DEVICE = "Device"
    DEVICES = "Devices"
