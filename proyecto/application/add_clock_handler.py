from application.dto.clock_request import ClockRequest
from domain.repository.IClockRepository import IClockRepository
from domain.entities.type_clock import TYPE_CLOCK
from domain.entities.clock import Clock
from uuid import uuid4
from datetime import datetime, timezone
from domain.repository.IClockRepository import IClockRepository

class AddClockHandler():

    def __init__(self,  repo:IClockRepository):
        self._repo = repo

    def run(self, request:ClockRequest):
        now = datetime.now(timezone.utc)
        clock = Clock(
            uuid4(),
            request.id,
            now,
            request.clock
        )

        user_clocks = self._repo.get_clocks_by_user(request.id)

        if user_clocks is None:
            result = self._repo.create_clocks(request.id)

        result = self._repo.add_clock(clock)
        return result

