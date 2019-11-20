from typing import Dict

from db import DB


class User:
    _db = DB()

    def __init__(self, data: Dict):
        self._id = data.get('_id')
        self._username = data.get('username')
        self._email = data.get('email')
        self._password = data.get('password')

    @property
    def id(self):
        return self._id

    @property
    def username(self):
        return self._username

    @property
    def email(self):
        return self._email

    @property
    def password(self):
        return self._password

