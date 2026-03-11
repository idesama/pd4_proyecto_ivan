import unittest
from infrastructure.user_repository import UserRepository
from application.create_user_handler import AddUserHandler
from application.get_user_handler import GetUserHandler
from application.commands.create_user_command import CreateUserCommand
from domain.user_service import UserService


class TestsUser(unittest.TestCase):

    def test_add_user_succes(self):
        user_repository = UserRepository()
        user_service = UserService(user_repository)
        handler = AddUserHandler(user_repository, user_service)
        command = CreateUserCommand(
            'Pedro',
            '0000',
            1
        )
        result = handler.run(command)
        self.assertEqual(result, True)


    def test_add_user_error(self):
        user_repository = UserRepository()
        user_service = UserService(user_repository)
        handler = AddUserHandler(user_repository, user_service)
        command1 = CreateUserCommand(
            'Abian',
            '0000',
            1
        )
        command2 = CreateUserCommand(
            'Abian',
            '0000',
            1
        )
        result1 = handler.run(command1)
        result2 = handler.run(command2)

        self.assertTrue(result1)
        self.assertFalse(result2)



    def test_get_user_by_username_succes(self):
        user_repository = UserRepository()
        user_service = UserService(user_repository)

        add_user_handler = AddUserHandler(user_repository, user_service)
        get_user_handler = GetUserHandler(user_repository)

        username = 'Ana'

        command = CreateUserCommand(
            username,
            '0000',
            1
        )
        result = add_user_handler.run(command)
        self.assertEqual(result, True)
        user = get_user_handler.run(username)
        self.assertTrue(user)
        self.assertEqual(user.username, username)


    def test_create_user_without_rol(self):
        user_service = UserService(UserRepository())
        user = user_service.create_user(
            'Pepe',
            '0000'  ,
            None   
        )
        self.assertEqual(user.rol, 2)

        