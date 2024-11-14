#!/usr/bin/env python3
'''module for Sesssion Authentication'''
from models.user import User
from .auth import Auth
import uuid


class SessionAuth(Auth):
    '''Inherits from Auth'''
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        '''creates a Session ID for a user_id:'''
        if user_id is None:
            return None
        if user_id is not str:
            return None
        else:
            session_id = uuid.uuid4()
            self.user_id_by_session_id[str(session_id)] = user_id
            return str(session_id)


    def user_id_for_session_id(self, session_id: str = None) -> str:
        '''returns a User ID based on session id'''
        if session_id is None or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        '''returns a User instance based on a cookie value'''
        session_cookie = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_cookie)
        user = User.get(user_id)
        return user
