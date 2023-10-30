#!/usr/bin/python3
"""This is documentation"""
import uuid


class BaseModel():

    def __init__(self):
        """Initialize variables"""

        self.id = str(uuid.uidd4())
        self.created_at = None
        self.updated_at = None

    def __str__(self):
        """__str__: should print: [<class name>]
        (<self.id>) <self.__dict__>"""

        return

    def save(self):
        """save(self): updates the public
        instance attribute updated_at with
        the current datetime"""

        return

    def to_dict(self):
        """to_dict(self): returns a dictionary containing
        all keys/values of __dict__ of the instance:

        by using self.__dict__, only instance attributes set will be returned
        a key __class__ must be added to this dictionary with the class name of the object
        created_at and updated_at must be converted to string object in ISO format:
            format: %Y-%m-%dT%H:%M:%S.%f (ex: 2017-06-14T22:31:03.285259)
            you can use isoformat() of datetime object
        This method will be the first piece of the serialization/deserialization process: create a dictionary representation with “simple object type” of our BaseModel"""
