from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'amdtelecom.settings')
app = Celery('amdtelecom')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

app.conf.beat_schedule = {
    'check-insurance-daily': {
        'task': 'insurance_expired',
        'schedule': crontab(hour='23')
    },
}

# celery -A amdtelecom worker -l info
# celery -A amdtelecom worker --beat --scheduler django --loglevel=info



# if settings.PROD:
#     app.config.update(
#         # CELERY CONF
#         CELERY_BROKER_URL = 'redis://localhost:6379'
#         CELERY_RESULT_BACKEND = 'redis://localhost:6379'
#         CELERY_ACCEPT_CONTENT = ['application/json']
#         CELERY_TASK_SERIALIZER = 'json'
#         CELERY_RESULT_SERIALIZER = 'json'
#         CELERY_TIMEZONE = 'Asia/Baku'
#     )
# else:
#     app.config.update(
#         CELERY_BROKER_URL = 'redis://localhost:6379'
#         CELERY_RESULT_BACKEND = 'redis://localhost:6379'
#         CELERY_ACCEPT_CONTENT = ['application/json']
#         CELERY_TASK_SERIALIZER = 'json'
#         CELERY_RESULT_SERIALIZER = 'json'
#         CELERY_TIMEZONE = 'Asia/Baku'
#     )