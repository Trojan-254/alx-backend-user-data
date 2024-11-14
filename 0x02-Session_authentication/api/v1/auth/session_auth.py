#!/usr/bin/env python3
'''module for Sesssion Authentication'''
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
