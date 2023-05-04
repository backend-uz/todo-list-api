# todo-list-api

## Description

This is a simple todo list API built with Flask and tinyDB. It is a REST API that allows you to create, read, update and delete tasks.

## Requirements

- users can create a task
- users can read a task
- users can delete a task
- users can mark a task as done
- users can mark a task as undone

## Database

The database is a simple JSON file that is created when the app is run for the first time. It is located in the root directory and is called `db.json`.

### Table

- Users
- Tasks

### Users

```json
{
    "users": {
        "chat_id": {
            "username": "username",
            "first_name": "first_name",
            "last_name": "last_name",
        }
    }
}
```

Users attributes:

| Attribute  | Type   | Required |
| ---------- | ------ | -------- |
| chat_id    | string | yes      |
| username   | string | no       |
| first_name | string | yes      |
| last_name  | string | no       |

### Tasks

```json
{
    "tasks": {
        "1": {
            "name": "title",
            "done": false,
            "chat_id": "chat_id"
        }
    }
}
```

Tasks attributes:

| Attribute   | Type    | Required |
| ----------- | ------- | -------- |
| title       | string  | yes      |
| done        | boolean | yes      |
| chat_id     | string  | yes      |

## Endpoints

Users endpoints:

| Method | Endpoint | Description |
| ------ | -------- | ----------- |
| POST   | /create-user   | Create a user |

Tasks endpoints:

| Method | Endpoint | Description |
| ------ | -------- | ----------- |
| GET    | /get-tasks/<chat_id>   | Get all tasks by chat_id |
| POST   | /create-task/<chat_id>  | Create a task |
| POST    | /mark-task/<chat_id>/<task_id> | Mark a task as done or undone |
| POST    | /delete-task/<chat_id>/<task_id> | Delete a task |

## API Documentation

### Create a user

**URL** : `/create-user`

**Method** : `POST`

**Request body**:

```json
{
    "chat_id": "chat_id",
    "username": "username",
    "first_name": "first_name",
    "last_name": "last_name"
}
```

### Create a task

**URL** : `/create-task/<chat_id>`
**Method** : `POST`

**Request body**:

```json
{
    "title": "title"
}
```

### Get all tasks by chat_id

**URL** : `/get-tasks/<chat_id>`
**Method** : `GET`

**Response body**:

```json
[
    {
        "name": "title",
        "done": false,
        "chat_id": "chat_id"
    }
]
```

### Mark a task as done or undone

**URL** : `/mark-task/<chat_id>/<task_id>`
**Method** : `POST`

**Request body**:

```json
{
    "name": "title",
    "done": true,
    "chat_id": "chat_id"
}
```

### Delete a task

**URL** : `/delete-task/<chat_id>/<task_id>`
**Method** : `POST`
