from db import Connection


class CryptoToken:
    def __init__(self, email: str, key=None):
        self._email = email
        self._key = key

    @property
    def email(self):
        return self._email

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, value):
        self._key = value

    async def save(self):
        crypto_token = await self._get_crypto_token()
        if crypto_token:
            await self._update_key()
        else:
            await self._create_crypto_token()

    async def get_key(self):
        response = await self._get_crypto_token()
        self.key = response[0]['private_key']
        return self.key

    async def _create_crypto_token(self):
        async with Connection() as connect:
            return await connect.execute(
                '''INSERT INTO crypto_token(email, private_key)
                VALUES('$1', '$2') ''',
                self.email, self.key
            )

    async def _get_crypto_token(self):
        async with Connection() as connect:
            return await connect.fetch(
                '''SELECT *
                FROM crypto_token
                WHERE email='$1' ''',
                self.email
            )

    async def _update_key(self):
        async with Connection() as connect:
            return await connect.execute(
                '''UPDATE crypto_token
                SET private_key='$1'
                WHERE email='$2' ''',
                self.key,
                self.email
            )
