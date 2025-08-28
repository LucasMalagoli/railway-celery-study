from .tasks import celery
from celery.schedules import crontab

# Configure periodic tasks
celery.conf.beat_schedule = {
    "say-hello-every-minute": {
        "task": "app.tasks.print_hello",
        "schedule": crontab(minute="*/1"),  # every 1 min
    },
}
