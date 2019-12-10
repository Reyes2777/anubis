import hashlib
import binascii
import os


def hash_password(pwd):
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwd_hash = hashlib.pbkdf2_hmac('sha512', pwd.encode('utf-8'), salt, 100000)
    pwd_hash = binascii.hexlify(pwd_hash)
    return (salt + pwd_hash).decode('ascii')


def verify_password(stored_pwd, provided_pwd):
    """Verify a stored password against one provided by user"""
    salt = stored_pwd[:64]
    stored_password = stored_pwd[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512', provided_pwd.encode('utf-8'), salt.encode('ascii'), 100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_password
