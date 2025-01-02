# Auth User Created Services


import secrets
from utils.constants import PASSWORD_LENGTH
from utils.utils import get_model

AvailableLeave = get_model(app_name="leave", model_name="AvailableLeave")


class AuthUserCreatedServices:
    def __init__(self, user):
        self.user = user

    def _generate_password(self):
        """Generate Password"""

        password = secrets.token_urlsafe(PASSWORD_LENGTH)
        self.user.set_password(password)
        # self.user.set_password("1234")
        self.user.save(update_fields=["password"])
        return password

    def create_user_leaves(self):
        """Create User Leaves"""
        AvailableLeave.objects.create(user=self.user)
        print("User Leaves Created")

    def send_registration_mail(self, password):
        """Send Registration Mail"""
        from users.tasks import registration_mail

        registration_mail.delay(self.user.id, password)
        return True

    def organization_head_registered(self):
        """Organization head Registered Successfully"""
        #  TODO: Complete Organization Head Registeration Mail
