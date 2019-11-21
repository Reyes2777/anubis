from models.user import User
from utils import validity_mail


class UserController:
    def create_user(self, email, pwd, username=None):
        if validity_mail(email):
            user = User()
            user.email = email
            user.password = pwd
            user.username = username
            try:
                user.save()
            except Exception as error:
                print(error)
        else:
            return None, 'email is not valid'



