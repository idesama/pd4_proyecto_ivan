from abc import ABC, abstractmethod
from domain.entities.clock import Clock

class IClockRepository(ABC):
    
    @abstractmethod
    def add_clock(self, clock:Clock):
        pass

    @abstractmethod
    def get_clocks_by_user(self, user_id)->list[Clock]:
        pass

    @abstractmethod
    def create_clocks(self, clock: Clock):
        pass