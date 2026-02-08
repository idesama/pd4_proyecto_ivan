from datetime import datetime
from domain.entities.type_clock import TYPE_CLOCK
from uuid import uuid4 

class Clock:
    def __init__(self, id: uuid4, id_user: uuid4, date: datetime, type: TYPE_CLOCK):
        self.id = id
        self.date = date
        self.type = type
        self.id_user = id_user
