#!/usr/bin/env python3
"""
Module for Session Authentication
"""


from .auth import Auth

from models.user import User
from uuid import uuid4


class SessionAuth(Auth):
    """Inherits from Auth
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """creates a session id for a user_id

        Args:
            request(_type_, optional): _description_. Defaults to none.

        Returns:
            _type_: _description_
        """
        if user_id is None or not isinstance(user_id, str):
            return None

        id = uuid4()
        self.user_id_by_session_id[str(id)] = user_id
        return str(id)

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Returns a user id based on session id

        Args:
            session_id (str, optional): _description_. Defaults to None.

        Returns:
                str: _description_
        """
        if session_id is None or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """returns a user instance based on cookie value

        Args:
            request (_type_, optional): _description_. Defaults to None.
        """
        session_cookie = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_cookie)
        user = User.get(user_id)
        return user

    def destroy_session(self, request=None):
        """deletes the user session/logout

        Args:
            request (_type_, optional): _description_. Defaults to None.

        Returns:
            _type_: _description_
        """
        if request is None:
            return False
        session_cookie = self.session_cookie(request)
        if session_cookie is None:
            return False
        user_id = self.user_id_for_session_id(session_cookie)
        if user_id is None:
            return False
        del self.user_id_by_session_id[session_cookie]
        return True
