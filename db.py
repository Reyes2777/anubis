import os

from pymongo import MongoClient
from settings import MONGO_DB_NAME, MONGO_HOST, MONGO_PORT, MONGO_PWD, MONGO_USER


class DB:
    _intance = None
    _inizialized = None
    _user_collection = None

    def __new__(cls, *args, **kwargs):
        if cls._intance is None:
            cls._intance = super().__new__(cls)
        return cls._intance

    def initialized(self):
        if self._inizialized is True:
            return None
        client = MongoClient(f'mongodb: //{MONGO_USER}:{MONGO_PWD}@{MONGO_HOST}:{MONGO_PORT}/{MONGO_DB_NAME}')
        data_base = client[MONGO_DB_NAME]
        self._user_collection = data_base['user']
        self._inizialized = True

    @property
    def user_collection(self):
        return self._user_collection
