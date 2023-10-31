#!/usr/bin/python3
"""This is documentation"""
import uuid


class BaseModel():

    def __init__(self):
        """Initialize variables"""
        
        form = "%Y-%m-%dT%H:%M:%S.%f"
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

        #dict["created_at"] = self.creatade_at.isoformat()
        #dict["update_at"] = self.update_at.isoformat()
        #dict["__class__"] = self.__class__
        """to_dict(self): returns a dictionary containing
        all keys/values of __dict__ of the instance:

        by using self.__dict__, only instance attributes set will be returned
        a key __class__ must be added to this dictionary with the class name of the object
        created_at and updated_at must be converted to string object in ISO format:
            format: %Y-%m-%dT%H:%M:%S.%f (ex: 2017-06-14T22:31:03.285259)
            you can use isoformat() of datetime object
        This method will be the first piece of the serialization/deserialization process: create a dictionary representation with “simple object type” of our BaseModel"""




"""Tasks 4 Update models/base_model.py:

    __init__(self, *args, **kwargs):
        you will use *args, **kwargs arguments for the constructor of a BaseModel. (more information inside the AirBnB clone concept page)
        *args wont be used
        if kwargs is not empty:
            each key of this dictionary is an attribute name (Note __class__ from kwargs is the only one that should not be added as an attribute. See the example output, below)
            each value of this dictionary is the value of this attribute name
            Warning: created_at and updated_at are strings in this dictionary, but inside your BaseModel instance is working with datetime object. You have to convert these strings into datetime object. Tip: you know the string format of these datetime
        otherwise:
            create id and created_at as you did previously (new instance)
"""
