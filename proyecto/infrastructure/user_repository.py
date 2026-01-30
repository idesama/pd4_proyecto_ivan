from domain.repository.IUserRepository import IUserRepository
from infrastructure.db import DB

class UserRepository(IUserRepository):
    
    def __init__(self, conection_db=DB()):
        self.conection_db = conection_db

    def add_user(self, user):
        self.conection_db.users[user.username] = user
        return True

    def get_user_by_username(self, username):
        return self.conection_db.users.get(username, None)
    
