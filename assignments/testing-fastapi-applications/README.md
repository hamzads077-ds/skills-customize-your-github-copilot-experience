# 📘 Assignment: Testing FastAPI Applications with pytest

## 🎯 Objective

Learn how to test Python applications with pytest and FastAPI's `TestClient`. You will write automated tests for successful API requests, validation failures, and missing resources.

## 📝 Tasks

### 🛠️ Write Tests for Successful Requests

#### Description
Use the provided FastAPI application and pytest starter file to test the API's basic behavior. Start by checking that the health-check and task-list routes return the expected responses.

#### Requirements
Completed program should:

- Create a `TestClient` for the FastAPI application
- Test that `GET /` returns a `200` status code
- Test that `GET /` returns the expected health-check message
- Test that `GET /tasks` returns a list of tasks
- Run the tests successfully with `pytest`


### 🛠️ Test Errors and Validation

#### Description
Add tests for the API's error behavior. Good tests should confirm that the API rejects invalid requests and clearly reports missing resources.

#### Requirements
Completed program should:

- Test that requesting an unknown task ID returns `404`
- Test that creating a task without a required title returns `422`
- Test that a valid task can be created with `POST /tasks`
- Use clear test names that describe each behavior


### 🛠️ Test a Complete CRUD Workflow

#### Description
Combine your tests into a workflow that creates, reads, updates, and deletes a task. Keep the workflow isolated so each test run starts with predictable data.

#### Requirements
Completed program should:

- Test creating a task and capture its returned ID
- Test retrieving the created task with `GET /tasks/{task_id}`
- Test updating the task with `PUT /tasks/{task_id}`
- Test deleting the task with `DELETE /tasks/{task_id}`
- Verify the task is no longer available after deletion
