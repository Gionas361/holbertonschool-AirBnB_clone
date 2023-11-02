#!/usr/bin/python3
"""Defines the BaseModel class."""
import models
from uuid import uuid4
import uuid
from datetime import datetime


class BaseModel:
    """Represents the BaseModel of the HBnB project."""

    def __init__(self, *args, **kwagrs):
        """Initialize variables"""

        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = None
        self.updated_at = None

    def __str__(self):
        """__str__: should print: [<class name>]
        (<self.id>) <self.__dict__>"""

        return

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel.

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tform)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):

        dict = self.__dict__.copy()
        dict["created_at"] = self.creatade_at.isoformat()
        dict["update_at"] = self.update_at.isoformat()
        dict["__class__"] = self.__class__.__name__
        return dict

    def __str__(self):
        """Return the print/str representation of the BaseModel instance."""
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)
