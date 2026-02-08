from domain.repository.IClockRepository import IClockRepository


class GetUserClockHandler():

    def __init__(self,  repo:IClockRepository):
        self._repo = repo

    def run(self, user_id:str):
        return self._repo.get_clocks_by_user(user_id)      


