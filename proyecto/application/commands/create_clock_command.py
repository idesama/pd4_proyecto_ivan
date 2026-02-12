from dataclasses import dataclass

@dataclass
class CreateClockCommand:
    id: str
    clock: int