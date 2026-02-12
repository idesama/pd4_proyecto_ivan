from domain.repository.IUserRepository import IUserRepository
from domain.entities.user import User
from dataclasses import asdict


class GetUserHandler():

    def __init__(self,  repo:IUserRepository):
        self._repo = repo

    def run(self, user_name:str):
        user = self._repo.get_user_by_username(user_name)
        return user


