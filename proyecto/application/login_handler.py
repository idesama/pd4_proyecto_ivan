from domain.repository.IUserRepository import IUserRepository
from application.commands.login_command import LoginCommand


class LoginHandler():

    def __init__(self,  repo:IUserRepository):
        self._repo = repo


    def run(self, command:LoginCommand):
        user = self._repo.get_user_by_username(command.username)
        if user and user.password == command.password:
            return user
        return None

