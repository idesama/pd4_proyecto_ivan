# handlers
from application.login_handler import LoginHandler
from application.create_user_handler import AddUserHandler
from application.get_user_handler import GetUserHandler
from application.create_clock_handler import AddClockHandler
from application.get_user_clocks_handler import GetUserClockHandler
# commands
from application.commands.login_command import LoginCommand
from application.commands.create_user_command import CreateUserCommand
from application.commands.create_clock_command import CreateClockCommand
# others
from domain.constants.type_clock import TYPE_CLOCK



def init_menu(
        login_handler: LoginHandler,
        add_user_handler: AddUserHandler,
        get_user_handler: GetUserHandler,
        add_clock_handler: AddClockHandler,
        get_user_clocks_handler: GetUserClockHandler
):
    intentos = 0
    acceso = False
    while intentos < 3:
        print("--- Sistema de Gestión de Fichajes ---")
        print('pruebas: admin - 1234')
        username = input('Ingrese su usuario: ')
        password = input('Ingrese su contraseña: ')
        login_request = LoginCommand(username, password)
        acceso = login_handler.run(login_request)

        if acceso is not None:

            salir = False
            user = get_user_handler.run(username)
            user = user.get_dto()
            while not salir:

                if user['rol'] == 1:
                    print('1. Añadir nuevo usuario')
                    print('2. Buscar usuario')
                    print('3. para fichar entrada')
                    print('4. para mostrar fichajes')
                    print('0. Salir')
                else:
                    print('3. para fichar entrada')
                    print('4. para mostrar fichajes')
                    print('0. Salir')

                try:
                    opcion = int(input('Introduce la opcion: '))
                except ValueError as e:
                    print('La opcion introducida no es válida, vuelve a intentarlo.')
                    continue
                
                if opcion == 1 and user['rol'] == 1:
                    user_name = input('Introduce el nombre: ')
                    password = input('Introduce la contraseña: ')
                    print('Introduce el rol (1 para administrador) (2 para usuario):')
                    print('(1/2)')
                    rol = int(input(''))
                    command = CreateUserCommand(
                        user_name,
                        password,
                        rol
                    )
                    result =  add_user_handler.run(command)
                    if result:
                        print('Usuario registrado correctamente.')
                elif opcion == 2 and user['rol'] == 1:
                    username = input('Introduce el nombre: ')
                    search_user = get_user_handler.run(username)
                
                    if search_user is None:
                        print('Usuario no encontrado.')
                    else:
                        print(search_user.get_dto())


                elif opcion == 3:
                    #TODO fichar entrada
                    command = CreateClockCommand(
                        user['id'],
                        TYPE_CLOCK.IN.value 
                    )
                    result = add_clock_handler.run(command)     
                    if not result :     
                        print("Operación fallida.")     
                    print("Fichaje realizado.")
                elif opcion == 4:
                    #TODO listar fichajes
                    result = get_user_clocks_handler.run(user['id'])
                    dtos = [e.get_dto() for e in result]
                    print(dtos)
                elif opcion == 0:
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