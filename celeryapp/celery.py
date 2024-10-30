# django_celery/celery.py

import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "celeryapp.settings")
app = Celery("celeryapp")

app.conf.beat_schedule = {
    'my-scheduled-task': {
        'task': 'emails.tasks.my_scheduled_task',
        'schedule':  crontab(minute='*/5'),  # Ejecutar cada 5 minutos
    },
}

app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
