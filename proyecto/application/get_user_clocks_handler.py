from domain.repository.IClockRepository import IClockRepository
from domain.entities.clock import Clock

class GetUserClockHandler():

    def __init__(self,  repo:IClockRepository):
        self._repo = repo

    def run(self, user_id:str)->list[Clock]:
        result = self._repo.get_clocks_by_user(user_id) 
        return result     


