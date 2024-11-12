#!/usr/bin/env python3
"""module for basic_auth"""
import base64
from flask import Flask
from typing import TypeVar
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """Inherits from basic auth"""
    pass
