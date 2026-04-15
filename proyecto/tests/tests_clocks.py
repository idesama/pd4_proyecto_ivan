import unittest
from infrastructure.clock_repository import ClockRepository
from infrastructure.db_tests import DBTests
from domain.clock_service import ClockService
from application.create_clock_handler import AddClockHandler
from application.commands.create_clock_command import CreateClockCommand
from domain.constants.type_clock import TYPE_CLOCK


class TestsClocks(unittest.TestCase):

    def test_create_clock_returns_clock_with_expected_fields(self):
        repository = ClockRepository(DBTests())
        service = ClockService(repository)

        user_id = 'user-123'
        clock = service.create_clock(user_id, TYPE_CLOCK.IN.value)

        self.assertEqual(clock.id_user, user_id)
        self.assertEqual(clock.type, TYPE_CLOCK.IN.value)
        self.assertIsNotNone(clock.date)
        self.assertTrue(hasattr(clock, 'id'))

    def test_have_clocks_returns_false_when_user_has_no_clocks(self):
        repository = ClockRepository(DBTests())
        service = ClockService(repository)

        user_id = 'missing-user'
        self.assertFalse(service.have_clocks(user_id))

    def test_have_clocks_returns_true_when_user_exists_even_if_list_empty(self):
        db = DBTests()
        db.clocks['user-empty'] = []
        repository = ClockRepository(db)
        service = ClockService(repository)

        self.assertTrue(service.have_clocks('user-empty'))
    

    def test_add_clock_handler_creates_clock_list_and_adds_clock(self):
        db = DBTests()
        repository = ClockRepository(db)
        service = ClockService(repository)
        handler = AddClockHandler(repository, service)

        user_id = 'new-user'
        command = CreateClockCommand(user_id, TYPE_CLOCK.OUT.value)

        result = handler.run(command)
        self.assertTrue(result)
        self.assertIn(user_id, db.clocks)
        self.assertEqual(len(db.clocks[user_id]), 1)
        stored_clock = db.clocks[user_id][0]
        self.assertEqual(stored_clock.id_user, user_id)
        self.assertEqual(stored_clock.type, TYPE_CLOCK.OUT.value)
