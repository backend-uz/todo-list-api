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
