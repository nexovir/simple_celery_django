# simple_celery/celery.py
import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "simple_celery.settings")

app = Celery("simple_celery")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

app.conf.update(
    task_time_limit=86400,
    task_soft_time_limit=86000,
    task_acks_late=True,
    worker_prefetch_multiplier=1,
    broker_transport_options={
        "visibility_timeout": 86400,
    }
)
