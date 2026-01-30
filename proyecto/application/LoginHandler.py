from domain.repository.IUserRepository import IUserRepository
from application.dto.login_request import LoginRequest


class LoginHandler():

    def __init__(self,  repo:IUserRepository):
        self._repo = repo


    def run(self, request:LoginRequest,):
        user = self._repo.get_user_by_username(request.username)
        if user and user.password == request.password:
            return user
        return None

