from dataclasses import dataclass

@dataclass
class ClockRequest:
    id: str
    clock: int