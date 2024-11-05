import os
from celery import Celery
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.dev")

app = Celery("quickpnr")

app.config_from_object("django.conf:settings", namespace="CELERY")


# Load tasks from all registered Django app configs.
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
