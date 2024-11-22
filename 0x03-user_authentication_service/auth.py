#!/usr/bin/env python3
"""module for authentication
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound

def _hash_password(password: str):
        """takes password as an arg
        returns bytes"""
        password_bytes = password.encode('utf-8')
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password_bytes, salt)
        return hashed_password


class Auth:
    """Auth class to interact with authentication database.
    """

    def __init__(self):
        self._db = DB

    def register_user(self, email: str, password: str) -> User:
        """takes mandatory email and password args
        returns a User object"""
        try:
            user_exists = self._db.find_user_by(email=email)
        except NoResultFound:
            new_user = self._db.add_user(email, _hash_password(password))
            return new_user
        raise ValueError('User {} already exists'.format(email))

