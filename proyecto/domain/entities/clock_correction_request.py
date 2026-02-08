from domain.entities.request_base import RequestBase
from domain.entities.clock import Clock
from dataclasses import dataclass

@dataclass
class ClockCorrectionRequest(RequestBase):
    clock: Clock
    clock_update: Clock
