from abc import abstractmethod, ABC
from domain.entities.user import User

class IUserRepository(ABC):
    
    @abstractmethod
    def add_user(self, user) -> bool:
        pass

    @abstractmethod
    def get_user_by_username(self, username)-> User | None:
        pass