from domain.repository.IUserRepository import IUserRepository
from domain.entities.user import User
from infrastructure.db import DB

class UserRepository(IUserRepository):
    
    def __init__(self, conection_db=DB()):
        self.conection_db = conection_db

    def add_user(self, user:User):
        user_clocks = self.conection_db.clocks.get(user.id, None)
        if user_clocks is None:
            self.conection_db.clocks[str(user.id)] = []
        self.conection_db.users[user.username] = user
        return True
    

    def get_user_by_username(self, username):
        return self.conection_db.users.get(username, None)
    
