from fastapi import FastAPI, HTTPException, status
from fastapi.testclient import TestClient
from pydantic import BaseModel

app = FastAPI(title="Testable Task API")


class TaskInput(BaseModel):
    title: str
    description: str = ""
    completed: bool = False


tasks = [
    {"id": 1, "title": "Learn pytest", "description": "Write an API test", "completed": False},
]


@app.get("/")
def read_root():
    return {"message": "Testable Task API is running"}


@app.get("/tasks")
def read_tasks():
    return tasks


@app.get("/tasks/{task_id}")
def read_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")


@app.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_task(task: TaskInput):
    new_task = task.model_dump()
    new_task["id"] = max((item["id"] for item in tasks), default=0) + 1
    tasks.append(new_task)
    return new_task


@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: TaskInput):
    for existing_task in tasks:
        if existing_task["id"] == task_id:
            existing_task.update(task.model_dump())
            return existing_task
    raise HTTPException(status_code=404, detail="Task not found")


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for index, task in enumerate(tasks):
        if task["id"] == task_id:
            tasks.pop(index)
            return {"message": "Task deleted"}
    raise HTTPException(status_code=404, detail="Task not found")


client = TestClient(app)


# TODO: Add pytest tests below.
# Example:
# def test_read_root():
#     response = client.get("/")
#     assert response.status_code == 200
