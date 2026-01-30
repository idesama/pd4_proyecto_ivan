from infrastructure.UserRepository import UserRepository
from application.LoginHandler import LoginHandler   
from application.add_user_handler import AddUserHandler
from application.get_user_handler import GetUserHandler
from presentation.menu import init_menu


def main(): 
    # instancio los handlers con sus respectivos repos
    login_handler = LoginHandler(UserRepository())
    add_user_handler = AddUserHandler(UserRepository())
    get_user_handler = GetUserHandler(UserRepository())
    
    # los inyecto desde aquí al menu
    init_menu(
        login_handler,
        add_user_handler,
        get_user_handler
    )
 
if __name__ == "__main__":
    main()