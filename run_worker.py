import os
from app.tasks import celery

if __name__ == "__main__":
    print("Starting worker...")
    print("REDIS_URL =", os.getenv("REDIS_URL"))
    celery.worker_main(["worker", "--loglevel=info"])
