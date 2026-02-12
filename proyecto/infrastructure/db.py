from domain.entities.user import User   
from domain.constants.user_rol import USER_ROL   
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
            admin = User('6d976e5f-85ab-4bce-8c0f-aa9270eaa308', "admin", "1234", USER_ROL.ADMIN.value, True, {})
            self.users = {admin.username: admin}
            self.clocks = {'6d976e5f-85ab-4bce-8c0f-aa9270eaa308': []}
            self.initialized = True
