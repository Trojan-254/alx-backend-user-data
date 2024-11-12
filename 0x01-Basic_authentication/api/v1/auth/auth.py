#!/usr/bin/env python3
"""module for managing API Authentication
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Class template for all authentication system"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """returns False
        path and excluded_paths to be used later"""
        if path is None:
            return True

        if excluded_paths is None or excluded_paths == []:
            return True

        if path in excluded_paths:
            return False

        for excluded_path in excluded_paths:
            if excluded_path.startswith(path):
                return False
            elif path.startswith(excluded_path):
                return False
            elif excluded_path[-1] == "*":
                if path.startswith(excluded_path[:-1]):
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        """returns None
        request will be the Flask request object"""
        if request is None:
            return None

        header = request.headers.get('Authorization')

        if header is None:
            return None

        return header

    def current_user(self, request=None) -> TypeVar('User'):
        """returns None
        request will be the Flask request object"""
        return None
