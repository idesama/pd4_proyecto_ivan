from domain.entities.user import User   
from domain.constants.user_rol import USER_ROL   

class DBTests:
    
    def __init__(self):
        admin = User('6d976e5f-85ab-4bce-8c0f-aa9270eaa308', "admin", "1234", USER_ROL.ADMIN.value, True, {})
        self.users = {admin.username: admin}
        self.clocks = {'6d976e5f-85ab-4bce-8c0f-aa9270eaa308': []}
 
