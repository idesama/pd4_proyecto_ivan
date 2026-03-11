from domain.constants.type_clock import TYPE_CLOCK
from domain.entities.clock import Clock
from domain.repository.IClockRepository import IClockRepository 
from uuid import uuid4
from datetime import datetime, timezone

class ClockService:

    def __init__(self, repo:IClockRepository):
        self._repo = repo
        
    def create_clock(self, user_id:str, type_clock:int):
        now = datetime.now(timezone.utc)
        clock = Clock(
            str(uuid4()),
            user_id,
            now,
            type_clock
        )
        return clock
    
    def have_clocks(self, user_id:str):
        '''
        Este método se borrará cuando implementemos la bbdd
        solo se usa para crear la lista en el diccionario que hace
        de bbdd temporal
        '''
        user_clocks = self._repo.get_clocks_by_user(user_id)
        if user_clocks is None:
            return False
        return True
         


