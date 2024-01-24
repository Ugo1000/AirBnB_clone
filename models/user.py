#!/usr/bin/python3
"""This module creates a User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """Class for managing user objects"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""


# usr = User("Ugo")
# usr.first_name = "sam"
# usr.id = 11
# usr.email = "sam@yahoo.com"
# usr.save()
# # print(usr)