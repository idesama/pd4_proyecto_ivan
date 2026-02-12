from dataclasses import dataclass

@dataclass
class GetUserClocksRequest:
    user_id: str
    filter: dict
