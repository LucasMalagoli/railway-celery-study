import os
from celery import Celery

# Railway provides REDIS_URL as an environment variable
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")

celery = Celery(
    "worker",
    broker=REDIS_URL,
    backend=REDIS_URL
)


@celery.task
def add(x, y):
    return x + y


# Scheduled task
@celery.task
def print_hello():
    print("Hello from Celery Beat!")
