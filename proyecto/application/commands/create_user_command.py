from dataclasses import dataclass

@dataclass
class CreateUserCommand:
    user_name:str
    password:str
    rol:int
        
