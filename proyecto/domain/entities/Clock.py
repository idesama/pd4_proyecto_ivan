from datetime import datetime
from TypeClock import TYPE_CLOCK
from uuid import uuid4 

class Clock:
    def __init__(self, id: uuid4, date: datetime, type: TYPE_CLOCK, id_user: uuid4):
        self.id = id
        self.date = date
        self.type = type
        self.id_user = id_user
