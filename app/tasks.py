import os
import logging

from celery import Celery

logger = logging.getLogger(__name__)

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


@celery.task
def print_hello():
    logger.info("Hello from Celery Beat!")
