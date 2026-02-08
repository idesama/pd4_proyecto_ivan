from uuid import uuid4
from dataclasses import dataclass

@dataclass
class RequestBase:
    id: uuid4
    user_id: uuid4