from todo import app
from flask import request

from .db import DB

db = DB()


@app.route('/')
def index():
    return '<h1>app is working now!</h1>'


@app.route('/create-user', methods=['POST'])
def add_user():
    '''create a new user view'''
    # get data from request body
    data = request.get_json()
    
    # get all attribus:
    chat_id = data.get('chat_id', False)
    first_name = data.get('first_name', False)
    last_name = data.get('last_name', '')
    username = data.get('username', '')

    # cheking required attributes:
    if not chat_id and not first_name:
        return {'status': 'chat_id and first_name are required'}
    
    # insert user into database
    db.create_user(chat_id=chat_id, first_name=first_name, user_name=username, last_name=last_name)
    return {'status': 200}


@app.route('/create-task/<chat_id>', methods=['POST'])
def add_task(chat_id):
    '''create a new task'''
    # get data from request body
    data = request.get_json()
    
    # get all attribu
    name = data.get('name', False)

    if not name:
        return {'status': 'name is required'}
    
    task_doc_id = db.create_task(chat_id=chat_id, name=name)
    return {'task_doc_id': task_doc_id}


@app.route('/get-tasks/<chat_id>')
def get_all_tasks(chat_id):
    '''get all tasks'''
    # get tasks from database
    tasks = db.get_tasks(chat_id=chat_id)

    return tasks


@app.route('/mark-task/<chat_id>/<task_id>', methods=['POST'])
def mark(chat_id, task_id):
    '''mark task as done or undone'''
    print(chat_id, task_id)
    task = db.mark_task(chat_id=chat_id, task_id=task_id)

    if task:
        return dict(task)
    return {'status': 'does not exist'}


@app.route('/delete-task/<chat_id>/<task_id>', methods=['POST'])
def delete_task(chat_id, task_id):
    '''delete task'''
    task = db.delete_task(chat_id=chat_id, task_id=task_id)

    if task:
        return {'status': 200}

    return {'status': 'error'}