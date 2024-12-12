from django.apps import AppConfig


class OrganizationConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "organization"

    def ready(self) -> None:
        import organization.signals  # noqa: F401,E402

        return super().ready()
