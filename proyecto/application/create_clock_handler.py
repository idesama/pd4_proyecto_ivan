from application.commands.create_clock_command import CreateClockCommand
from domain.repository.IClockRepository import IClockRepository
from domain.entities.clock import Clock
from uuid import uuid4
from datetime import datetime, timezone
from domain.repository.IClockRepository import IClockRepository

class AddClockHandler():

    def __init__(self,  repo:IClockRepository):
        self._repo = repo

    def run(self, command:CreateClockCommand):
        now = datetime.now(timezone.utc)
        clock = Clock(
            uuid4(),
            command.id,
            now,
            command.clock
        )

        user_clocks = self._repo.get_clocks_by_user(command.id)

        if user_clocks is None:
            result = self._repo.create_clocks(command.id)

        result = self._repo.add_clock(clock)
        return result

