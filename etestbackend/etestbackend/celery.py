# django_celery/celery.py

import os
from celery import Celery
import ssl

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "etestbackend.settings")
app = Celery(
    "etestbackend",
    broker_use_ssl={"ssl_cert_reqs": ssl.CERT_NONE},
    redis_backend_use_ssl={"ssl_cert_reqs": ssl.CERT_NONE},
)
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
