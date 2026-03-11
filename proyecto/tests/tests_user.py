import unittest
from infrastructure.user_repository import UserRepository
from application.create_user_handler import AddUserHandler
from application.get_user_handler import GetUserHandler
from application.commands.create_user_command import CreateUserCommand


class TestsUser(unittest.TestCase):

    def test_add_user(self):
        handler = AddUserHandler(UserRepository)
        user = CreateUserCommand(
            'Abian',
            '0000',
            '1'
        )
        result = handler.run(user)
        self.assertEqual(result, True)




    def test_get_user_by_username(self):
        add_user_handler = AddUserHandler(UserRepository)
        get_user_handler = GetUserHandler(UserRepository)
        username = 'Ana'
        user = CreateUserCommand(
            username,
            '0000',
            2
        )
        result = add_user_handler.run(user)
        self.assertEqual(result, True)
        user = get_user_handler.run(username)
        self.assertTrue(user)
        self.assertEqual(user.username, username)

    def test_add_user_without_rol(self):
        add_user_handler = AddUserHandler(UserRepository)
        get_user_handler = GetUserHandler(UserRepository)
        username = 'Pedro'
        user = CreateUserCommand(
            username,
            '0000'
        )
        result = add_user_handler.run(user)
        self.assertEqual(result, True)
        user = get_user_handler.run(username)
        self.assertEqual(user.rol, 2)

        