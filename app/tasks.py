from celery import Celery
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Redis broker URL from Railway environment variable
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")

# Initialize Celery
app = Celery('tasks', broker=REDIS_URL, backend=REDIS_URL)


# ---- Example API-triggered task ----
@app.task
def add(a: int, b: int):
    logger.info(f"Adding {a} + {b}")
    return a + b


# ---- Periodic task ----
@app.task(name="print_hello")
def print_hello():
    logger.info("Hello from periodic task!")

# ---- Schedule periodic task programmatically ----
@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Run print_hello every 60 seconds
    sender.add_periodic_task(60, print_hello.s(), name="Say hello every minute")
