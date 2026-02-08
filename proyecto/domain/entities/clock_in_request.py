from domain.entities.request_base import RequestBase
from domain.entities.clock import Clock

class ClockInRequest(RequestBase):
    clock: Clock  