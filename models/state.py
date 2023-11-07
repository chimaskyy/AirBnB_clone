#!/usr/bin/python3
"""
Defines State Class, inherits from user.
"""

from .base_model import BaseModel


class User(BaseModel):
    """
    Defines User.
    """

    name = ""
