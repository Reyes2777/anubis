import logging

from models.user import User
from utils.email import validity_mail
from utils.crypto import hash_password

logger = logging.getLogger('anubis')


class UserController:
    def __init__(self, email=None, pwd=None):
        self._email = email
        self._pwd = pwd

    async def create_user(self, username=None):
        ok = False
        message = 'Email is not valid'
        if validity_mail(self._email):
            logger.info(f'Creating user: {self._email}')
            user = User()
            user.email = self._email
            user.password = hash_password(self._pwd)
            user.username = username
            try:
                user.save()
                message = f'User {self._email} created successfully'
                ok = True
                logger.info(message)
                return ok, message
            except Exception as error:
                message = f'User could not created for this reason: {error}'
                logger.error(message)
                return ok, message
        else:
            return ok, message

    async def get_user(self):
        user = User.objects(email=self._email).first()
        if user:
            logger.info(f'User {self._email} found')
            return user
        else:
            logger.info(f'User {self._email} not found')
