#!/usr/bin/python3
"""Defines the User class"""
from models.base_model import BaseModel

class Usuario(BaseModel):
    """Atribute:
    
    email (str): The email of the user.
    password (str): The password of the user.
    Frist_name (str): The frist name of the user.
    last_name (str): The last name of the user. """
    
    email = ""
    password = ""
    first_name = ""
    last_name = ""
