from domain.repository.IUserRepository import IUserRepository
from domain.entities.user import User
from infrastructure.db import DB
from proyecto.infrastructure.database import Database

class UserRepository(IUserRepository):
    
    def __init__(self, db=Database()):
        self.db = db

    def add_user(self, user:User)-> int:
        result = self.get_user_by_username(User.username)
        if result is not None:
            raise Exception
        query = "INSERT INTO users VALUES (?, ?, ?, ?, ?)"
        result = self.db.execute_wrapper(query,tuple(user.get_dto().values))
        return result

    def get_user_by_username(self, username:str):
        query = "SELECT FROM users WHERE username = ?"
        result = self.db.execute_wrapper(query,(username,))
        if result is None:
            return None
        user = User(*result)
        return user






    
