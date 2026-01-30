# handlers
from application.login_handler import LoginHandler
from application.add_user_handler import AddUserHandler
from application.get_user_handler import GetUserHandler
# dtos
from application.dto.login_request import LoginRequest
from application.dto.add_user_request import AddUserRequest
# entidades
from domain.entities.user import User
from domain.entities.user_rol import USER_ROL


def init_menu(
        login_handler: LoginHandler,
        add_user_handler: AddUserHandler,
        get_user_handler: GetUserHandler
):
    intentos = 0
    acceso = False
    while intentos < 3:
        print("--- Sistema de Gestión de Fichajes ---")
        print('pruebas: admin - 1234')
        username = input('Ingrese su usuario: ')
        password = input('Ingrese su contraseña: ')
        login_request = LoginRequest(username, password)
        acceso = login_handler.run(login_request)

        if acceso is not None:

            salir = False
            user: User = get_user_handler.run(username)
            while not salir:

                if user.rol ==  USER_ROL.ADMIN.value:
                    print('1. Añadir nuevo usuario')
                    print('2. Buscar usuario')
                    print('3. Salir')
                else:
                    print('3. Salir')

                try:
                    opcion = int(input('Introduce la opcion: '))
                except ValueError as e:
                    print('La opcion introducida no es válida, vuelve a intentarlo.')
                    continue
                
                if opcion == 1 and user.rol == USER_ROL.ADMIN.value:
                    user_name = input('Introduce el nombre: ')
                    password = input('Introduce la contraseña: ')
                    print('Introduce el rol (1 para administrador) (2 para usuario):')
                    print('(1/2)')
                    rol = input('')
                    request = AddUserRequest(
                        user_name,
                        password,
                        rol
                    )
                    result =  add_user_handler.run(request)
                    if result:
                        print('Usuario registrado correctamente.')
                elif opcion == 2 and user.rol == USER_ROL.ADMIN.value:
                    username = input('Introduce el nombre: ')
                    result = get_user_handler.run(username)
                    
                    if result is None:
                        print('Usuario no encontrado.')
                    else:
                        search_user: User = result 
                        print(f'Id: {search_user.id}')
                        print(f'Nombre: {search_user.username}')
                        print(f'Rol: {search_user.rol}')
                elif opcion == 3:
                    salir = True
                    print('Sesión cerrada.') 
                else:
                    print('Operacion no valida')

        else:
            intentos += 1
            print('Credenciales incorrectas')
            print(f'Intentos restantes: {3-intentos}')

    if not acceso:
        print('Ha superado el numero de intentos, vuelva mas tarde.')