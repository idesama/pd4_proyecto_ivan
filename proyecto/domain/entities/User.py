from domain.entities.UserRol import USER_ROL
from uuid import uuid4 
class User:
    def __init__(self, id:uuid4, username: str, password: str, rol: USER_ROL):
        self.id = id
        self.username = username
        self.password = password
        self.rol = rol
        self.active = True
        self.clocks = {}

