from abc import ABC, abstractmethod

class IClockRepository(ABC):
    
    @abstractmethod
    def add_clock(self, clock):
        pass

    @abstractmethod
    def get_clocks_by_user(self, user_id):
        pass