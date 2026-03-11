from uuid import uuid4
from domain.entities.user import User
from domain.constants.user_rol import USER_ROL
from domain.repository.IUserRepository import IUserRepository

class UserService:

    def __init__(self, repo:IUserRepository):
        self._repo = repo


    def create_user(self, username, password, rol):

        if not username or not password:
            raise ValueError("Username, password, or role cannot be empty")

        user = self._repo.get_user_by_username(username)
        if user is not None:
            raise ValueError("Ya existe el usuario en la base de datos")

        id = uuid4()
        # aunque el usurio no metiera un valor correcto para el rol
        # se le asignaria el rol mas básico de usuario para agilizar
        rol = USER_ROL.ADMIN.value if rol == '1' else USER_ROL.USER.value

        return User(
            id,
            username,
            password,
            rol,
            active= True,
            clocks= {}
            )
   