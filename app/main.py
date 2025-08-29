from fastapi import FastAPI
from app.tasks import add
from celery.result import AsyncResult

app = FastAPI()


@app.get("/add/")
async def add_numbers(a: int, b: int):
    task = add.delay(a, b)
    return {"task_id": task.id, "status": "submitted"}


@app.get("/task_status/{task_id}")
async def task_status(task_id: str):
    task_result = AsyncResult(task_id)
    return {"task_id": task_id, "status": task_result.status, "result": task_result.result}
