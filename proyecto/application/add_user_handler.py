from domain.repository.IUserRepository import IUserRepository
from domain.entities.User import User
from application.dto.add_user_request import AddUserRequest
from uuid import uuid4
from domain.entities.UserRol import USER_ROL


class AddUserHandler():

    def __init__(self,  repo:IUserRepository):
        self._repo = repo


    def run(self, request:AddUserRequest):
        user = self._repo.get_user_by_username(request.user_name)
        if user is not None:
            return False

        # aunque el usurio no metiera un valor correcto para el rol
        # se le asignaria el rol mas básico de usuario para agilizar
        rol = USER_ROL.ADMIN.value if request.rol == '1' else USER_ROL.USER.value

        user = User(
            id = uuid4(),
            username = request.user_name,
            password = request.password,
            rol= rol)

        result = self._repo.add_user(user)
        
        return result

