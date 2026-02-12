from domain.repository.IUserRepository import IUserRepository
from domain.entities.user import User
from application.commands.create_user_command import CreateUserCommand
from uuid import uuid4
from domain.constants.user_rol import USER_ROL


class AddUserHandler():

    def __init__(self,  repo:IUserRepository):
        self._repo = repo


    def run(self, command:CreateUserCommand):
        user = self._repo.get_user_by_username(command.user_name)
        if user is not None:
            return False

        # aunque el usurio no metiera un valor correcto para el rol
        # se le asignaria el rol mas básico de usuario para agilizar
        rol = USER_ROL.ADMIN.value if command.rol == '1' else USER_ROL.USER.value

        user = User(
            id = str(uuid4()),
            username = command.user_name,
            password = command.password,
            rol= rol,
            active= True,
            clocks= {}
            )

        result = self._repo.add_user(user)
        
        return result

