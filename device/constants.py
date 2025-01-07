"""Device App Constants"""

from django.utils.translation import gettext_noop as _


class AuthMessages:
    """Auth Messages"""

    USER_NOT_FOUND = _("User not found")
    UNAUTHORIZED_ACTION = _("You are not authorized to perform this action")
    _("Device is already acquired by another user.")
    ALREADY_ACQUIRED = _("Device is already acquired by another user.")
    NOT_ACQUIRED = _("Device is not acquired by any user.")


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
