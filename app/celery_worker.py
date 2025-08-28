from .tasks import celery

# Entrypoint for Celery worker
# Command: celery -A app.tasks worker --loglevel=info
