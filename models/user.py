#!/usr/bin/python3
"""This module defines a class user"""
from models.base_mode import BaseModel


class User(BaseModel):
    """This class defines a user by various attributes"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''
