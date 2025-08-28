from fastapi import FastAPI
from .tasks import add

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI + Celery on Railway!"}


@app.post("/add/")
def run_add(a: int, b: int):
    task = add.delay(a, b)
    return {"task_id": task.id}
