from mongoengine import connect
from settings import MONGO_PWD, MONGO_USER, MONGO_PORT, MONGO_HOST, MONGO_DB_NAME

connect(db=MONGO_DB_NAME, username=MONGO_USER, password=MONGO_PWD,
        host=f'mongodb://{MONGO_USER}:{MONGO_PWD}@{MONGO_HOST}:{MONGO_PORT}/{MONGO_DB_NAME}')