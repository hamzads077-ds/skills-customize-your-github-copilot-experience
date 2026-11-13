# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small task-management REST API with FastAPI. You will practice defining HTTP routes, validating request data with Pydantic models, and returning useful status codes and error messages.

## 📝 Tasks

### 🛠️ Create the API and Read Routes

#### Description
Use the provided starter code to run a FastAPI application. Add a root health-check route and routes that allow clients to retrieve all tasks and one task by its ID.

#### Requirements
Completed program should:

- Start with `uvicorn` and expose the API locally
- Return a short JSON message from `GET /`
- Return all tasks from `GET /tasks`
- Return one matching task from `GET /tasks/{task_id}`
- Return a `404` response when the requested task does not exist


### 🛠️ Add Validated Create and Update Operations

#### Description
Define a Pydantic model for incoming task data and use it to implement create and update operations. Each task should have a title, description, and completion status.

#### Requirements
Completed program should:

- Validate that a task title is present and not blank
- Accept new tasks with `POST /tasks` and return the created task with a unique ID
- Update an existing task with `PUT /tasks/{task_id}`
- Return a `201` status for successful task creation
- Return a `404` response when updating a task that does not exist


### 🛠️ Complete and Test the CRUD API

#### Description
Finish the API by adding task deletion and testing each endpoint through FastAPI’s interactive documentation at `/docs` or a REST client.

#### Requirements
Completed program should:

- Delete an existing task with `DELETE /tasks/{task_id}`
- Return a clear success response after deletion
- Return a `404` response when deleting a task that does not exist
- Demonstrate a complete create, read, update, and delete workflow
- Include at least three example requests and their expected responses in your submission
