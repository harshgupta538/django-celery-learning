from __future__ import absolute_import, unicode_literals
from operator import truediv
import os

from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'learnDjangoCelery.settings')

app = Celery('learnDjangoCelery')
app.conf.enable_utc = False

app.conf.update(timezone = 'Asia/Kolkata')
app.config_from_object(settings, namespace='CELERY')

# Celery Beat Settings

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print("Request", self.request)