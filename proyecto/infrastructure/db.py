from domain.entities.user import User   
from domain.entities.user_rol import USER_ROL   
from uuid import uuid4

class DB:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        # Esto solo se ejecuta la primera vez si lo controlas
        if not hasattr(self, "initialized"):
            admin = User(uuid4(), "admin", "1234", USER_ROL.ADMIN.value)
            self.users = {admin.username: admin}
            self.clocks = {}
            self.initialized = True
