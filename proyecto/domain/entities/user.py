from domain.entities.base_entity import IBaseEntity
from dataclasses import dataclass, asdict
from domain.constants.user_rol import USER_ROL
from uuid import uuid4 

@dataclass
class User(IBaseEntity):
    username:str
    password:str
    rol:USER_ROL
    active:bool
    clocks:dict

    def get_dto(self):
        return asdict(self)