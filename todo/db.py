from tinydb import TinyDB, Query
from tinydb.table import Document


class DB:
    def __init__(self) -> None:
        db = TinyDB('db.json', indent=4)
        self.users = db.table('users')
        self.tasks = db.table('tasks')

    
    def create_user(self, chat_id: str, first_name: str, user_name='', last_name='') -> bool:
        '''create a new user'''
        user_data = {
            'username': user_name,
            'first_name': first_name,
            'last_name': last_name
        }
        user_doc = Document(value=user_data, doc_id=chat_id)
        self.users.insert(user_doc)
        return True

