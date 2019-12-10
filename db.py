import logging

from mongoengine import connect
from settings import MONGO_DB_NAME, MONGO_HOST, MONGO_PORT, MONGO_PWD, MONGO_USER

logger = logging.getLogger('anubis')


async def run():
    connect(db=MONGO_DB_NAME, username=MONGO_USER, password=MONGO_PWD,
            host=f'mongodb://{MONGO_USER}:{MONGO_PWD}@{MONGO_HOST}:{MONGO_PORT}/{MONGO_DB_NAME}')
    logger.info(f'CONNECTED SUCCESSFULLY TO DATABASE:{MONGO_DB_NAME}')
