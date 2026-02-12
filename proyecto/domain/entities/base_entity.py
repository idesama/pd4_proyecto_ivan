from dataclasses import dataclass, asdict 
from abc import ABC, abstractmethod

@dataclass
class IBaseEntity(ABC):
    id:str

    @abstractmethod
    def get_dto(self)-> dict:
        pass