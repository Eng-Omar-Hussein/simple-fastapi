from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Task Protocol API", version="1.0.0")

# Mock database
fake_db = []

class TaskBase(BaseModel):
    title: str
    description: str | None = None

class TaskResponse(TaskBase):
    id: int

@app.get("/health", tags=["System"])
def read_health():
    """Endpoint for container orchestration readiness/liveness probes."""
    return {"status": "healthy"}

@app.post("/tasks/", response_model=TaskResponse, tags=["Tasks"])
def create_task(task: TaskBase):
    new_task = TaskResponse(id=len(fake_db) + 1, **task.model_dump())
    fake_db.append(new_task)
    return new_task

@app.get("/tasks/", response_model=List[TaskResponse], tags=["Tasks"])
def get_tasks():
    return fake_db
