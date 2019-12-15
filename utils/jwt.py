import crypt
import jwt


class JWT:

    def __init__(self):
        self.key = crypt.mksalt(crypt.METHOD_SHA256)

    def encrypt(self, data: dict):
        return jwt.encode(data, self.key, algorithm='HS256')

    def decrypt(self, token: str):
        return jwt.decode(token, self.key, algorithms='HS256')
        

