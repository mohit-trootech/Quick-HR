"""Quick PNR - Users App Constants"""

from django.utils.translation import gettext_lazy as _


class ModelFields:
    """Model Contants - Quick HR Users"""

    INACTIVE_STATUS = 0
    ACTIVE_STATUS = 1
    STATUS_CHOICES = (
        (INACTIVE_STATUS, _("Unverified")),
        (ACTIVE_STATUS, _("Verified")),
    )


# Profile Thumbnail Preview
THUMBNAIL_PREVIEW_TAG = '<img src="{img}" width="320"/>'
THUMBNAIL_PREVIEW_HTML = """<div class="warning" style="color:#000;width: 320px;
        padding: 12px;
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: start;
        background: #FEF7D1;
        border: 1px solid #F7C752;
        border-radius: 5px;
        box-shadow: 0px 0px 5px -3px #111;">
        <div class="warning__icon">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" viewBox="0 0 24 24" height="24" fill="none">
                <path fill="#393a37" d="m13 14h-2v-5h2zm0 4h-2v-2h2zm-12 3h22l-11-19z" style="
        fill: #F7C752;"></path>
            </svg>
        </div>
        <strong>No Profile Image Available</strong>
    </div>"""


# User Signup Messages
class UserRegistrationMessages:
    """User Registration Constants Messages"""

    PASSWORD_DOES_NOT_MATCH = _("Password does not match")
    EMAIL_EXIST_ERROR = _("Email already exists")
    USERNAME_ALREADY_EXISTS = _("Username already exists")


class AuthConstantsMessages:
    """Auth Constants Messages"""

    INVALID_EMAIL_OR_PASSWORD = _("Invalid email or password")
    USER_ALREADY_EXIST = _("User already exists with this email")
    PASSWORD_DOES_NOT_MATCH = _("Password does not match")
    NEW_PASSWORD_SAME_AS_OLD_PASSWORD = _("New password cannot be same as old password")
    INVALID_PASSWORD = _("Invalid password")
    EMAIL_REQUIRED = _("Email is required")
    EMAIL_VERIFIED_OTP_DELIVERED = _("OTP delivered to your email address")
    USE_NOT_FOUND = _("User not found")
    INVALID_OTP = _("Invalid OTP")
    EXPIRED_OTP = _("OTP has expired")
    CREDENTIALS_SEND_ON_MAIL = _("Your credentials has been send on your mail")


class ResponseMessages:
    """Users Messages Constants"""

    EMAIL_VERIFIED = _("Email verified successfully")
    PASSWORD_CHANGED_DONE = _("Password changed successfully")
    PASSWORD_RESET_DONE = _("Password reset successfully")
    USER_NOT_FOUND = _("User not found")


class VerboseNames:
    """User Models Verbose name"""

    PROFILE_IMAGE = _("Profile Image")
    EMAIL_ADDRESS = _("Email Address")
    VERIFICATION_STATUS = _("Verification Status")
    AGE = _("Age")
    ADDRESS = _("Address")
    GOOGLE_ID = _("Google ID")

    # Company Model

    COMPANY = "company"


class Choices:
    """User App Models Choices"""

    # Company Choices
    QUICKTECH = "quicktech"
    QUICKXOM = "quickxom"
    QUICKBOUND = "quickbound"
    COMPANY_CHOICES = (
        (QUICKTECH, _("Quicktech")),
        (QUICKXOM, _("Quickxom")),
        (QUICKBOUND, _("Quickbound")),
    )

    # Designation Choices
    JUNIOR = "junior"
    EXPERIENCED = "experienced"
    SENIOR = "senior"
    MANAGER = "manager"
    DESGINATION_CHOICES = (
        (JUNIOR, _("Junior")),
        (EXPERIENCED, _("Experienced")),
        (SENIOR, _("Senior")),
        (MANAGER, _("Manager")),
    )
