import asyncio
import asyncpg
import logging

from mongoengine import connect
from settings import MONGO_DB_NAME, MONGO_HOST, MONGO_PORT, MONGO_PWD, MONGO_USER, POSTGRES_DB_HOST, POSTGRES_DB_NAME,\
    POSTGRES_DB_PASSWORD, POSTGRES_DB_PORT, POSTGRES_DB_USER

logger = logging.getLogger('anubis')


async def run():
    connect(db=MONGO_DB_NAME, username=MONGO_USER, password=MONGO_PWD,
            host=f'mongodb://{MONGO_USER}:{MONGO_PWD}@{MONGO_HOST}:{MONGO_PORT}/{MONGO_DB_NAME}')
    logger.info(f'CONNECTED SUCCESSFULLY TO DATABASE:{MONGO_DB_NAME}')


class Connection:
    _db_host = POSTGRES_DB_HOST
    _db_name = POSTGRES_DB_NAME
    _db_password = POSTGRES_DB_PASSWORD
    _db_port = POSTGRES_DB_PORT
    _db_username = POSTGRES_DB_USER

    def __init__(self):
        self._con = None

    async def __aenter__(self) -> asyncpg.Connection:
        try:
            self._con = await asyncpg.connect(
                dsn=f'postgres://{self._db_username}:{self._db_password}@{self._db_host}:{self._db_port}/'
                    f'{self._db_name}',
                timeout=5
            )
            print('connection')
        except asyncio.TimeoutError:
            print('timeout connection error')
        return self._con

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print('closing')
        await self._con.close()