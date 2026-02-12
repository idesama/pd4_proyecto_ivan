from presentation.menu import init_menu
# repositories
from infrastructure.user_repository import UserRepository
from infrastructure.clock_repository import ClockRepository
# handlers
from application.login_handler import LoginHandler   
from application.create_user_handler import AddUserHandler
from application.get_user_handler import GetUserHandler
from application.create_clock_handler import AddClockHandler
from application.get_user_clocks_handler import GetUserClockHandler

def main(): 
    # instancio los handlers con sus respectivos repos
    login_handler = LoginHandler(UserRepository())
    add_user_handler = AddUserHandler(UserRepository())
    get_user_handler = GetUserHandler(UserRepository())
    add_clock_handler = AddClockHandler(ClockRepository())
    get_user_clocks_handler = GetUserClockHandler(ClockRepository())
    
    # los inyecto desde aquí al menu
    init_menu(
        login_handler,
        add_user_handler,
        get_user_handler,
        add_clock_handler,
        get_user_clocks_handler
    )

if __name__ == "__main__":
    main()