class CreateUserCommand:
    def __init__(self, user_name: str, password: str, rol: int):
        self.user_name = user_name
        self.password = password
        self.rol = rol
        
