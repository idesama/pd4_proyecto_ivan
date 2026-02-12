from domain.entities.base_entity import IBaseEntity
from dataclasses import dataclass
from domain.constants.user_rol import USER_ROL


@dataclass
class User(IBaseEntity):
    username:str
    password:str
    rol:USER_ROL
    active:bool
    clocks:dict

