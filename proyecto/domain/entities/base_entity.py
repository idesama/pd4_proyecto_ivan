from dataclasses import dataclass, asdict 

@dataclass
class IBaseEntity():
    id:str

    def get_dto(self)-> dict:
        return asdict(self)