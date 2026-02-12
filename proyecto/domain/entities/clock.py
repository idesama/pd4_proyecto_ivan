from domain.entities.base_entity import IBaseEntity
from dataclasses import dataclass, asdict
from datetime import datetime
from domain.constants.type_clock import TYPE_CLOCK


@dataclass
class Clock(IBaseEntity):
    id_user:str
    date:datetime
    type:TYPE_CLOCK

    def get_dto(self):
        return asdict(self)