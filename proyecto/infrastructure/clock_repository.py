from domain.entities.clock import Clock
from domain.repository.IClockRepository import IClockRepository
from infrastructure.db import DB

class ClockRepository(IClockRepository):
    
    def __init__(self, conection_db=DB()):
        self.conection_db = conection_db

    def add_clock(self, clock: Clock):
        self.conection_db.clocks[str(clock.id_user)].append(clock)
        return True
    
    def create_clocks(self, clock: Clock):
        self.conection_db.clocks[str(clock.id_user)] = []
        return True
           
    def get_clocks_by_user(self, user_id):
        return self.conection_db.clocks.get(user_id, None)



