import os
from celery import Celery


# Set default Django settings module for the "celery" program
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myshop.settings")

app = Celery("myshop")

# Import settings from settings with CELERY_ prefix
app.config_from_object("django.conf:settings", namespace="CELERY")
# Search all tasks in apps
app.autodiscover_tasks()
