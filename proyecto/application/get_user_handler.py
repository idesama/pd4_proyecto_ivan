from domain.repository.IUserRepository import IUserRepository
from application.dto.add_user_request import AddUserRequest


class GetUserHandler():

    def __init__(self,  repo:IUserRepository):
        self._repo = repo

    def run(self, request:str):
        user = self._repo.get_user_by_username(request)      
        return user

