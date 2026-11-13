from fastapi import FastAPI

app = FastAPI(title="Task API")

tasks = [
    {"id": 1, "title": "Learn FastAPI", "description": "Build the first route", "completed": False},
    {"id": 2, "title": "Test the API", "description": "Use the interactive docs", "completed": False},
]


@app.get("/")
def read_root():
    return {"message": "Task API is running"}


# TODO: Add a GET /tasks route that returns every task.


# TODO: Add a GET /tasks/{task_id} route.
# Return a 404 error when task_id does not match a task.


# TODO: Define a Pydantic model for task input.


# TODO: Add POST /tasks and return the new task with status code 201.


# TODO: Add PUT /tasks/{task_id} to update an existing task.


# TODO: Add DELETE /tasks/{task_id} to remove an existing task.


# Run with:
# uvicorn starter-code:app --reload
