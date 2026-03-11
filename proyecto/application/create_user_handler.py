from domain.repository.IUserRepository import IUserRepository
from domain.user_service import UserService
from application.commands.create_user_command import CreateUserCommand

class AddUserHandler():

    def __init__(self,  repo:IUserRepository, user_service: UserService):
        self._repo = repo
        self.user_service = user_service
       
    def run(self, command:CreateUserCommand):

        try:
            user = self.user_service.create_user(
                command.user_name,
                command.password,
                command.rol
            )
        except ValueError as e:
            print(e)
            return False
    
        result = self._repo.add_user(user)
        
        return result

