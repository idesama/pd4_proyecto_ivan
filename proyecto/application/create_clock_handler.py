from application.commands.create_clock_command import CreateClockCommand
from domain.repository.IClockRepository import IClockRepository
from domain.entities.clock import Clock
from domain.clock_service import ClockService
from uuid import uuid4
from datetime import datetime, timezone
from domain.repository.IClockRepository import IClockRepository

class AddClockHandler():

    def __init__(self,  repo:IClockRepository, clock_service:ClockService):
        self._repo = repo
        self.clock_service = clock_service

    def run(self, command:CreateClockCommand):
        
        clock = self.clock_service.create_clock(
            command.id,
            command.clock
        )

        have_clocks = self.clock_service.have_clocks(command.id)
        if not have_clocks:
            result = self._repo.create_clocks(command.id)

        result = self._repo.add_clock(clock)
        return result

