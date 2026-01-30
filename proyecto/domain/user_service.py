from uuid import uuid4
from domain.entities.user import User

class UserService:
    def create_user(self, username, password, rol):
        """Create a new user with the given username, password, and role."""
        id = uuid4()
        if username and password and rol:
            return User(id, username, password, rol)
        else:
            raise ValueError("Username, password, and role cannot be empty")    