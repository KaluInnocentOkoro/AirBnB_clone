#!/usr/bin/python3
"""A BaseModel class"""
from datetime import datetime
import uuid


class BaseModel:
    """Defines a base model class"""

    def __init__(self, *args, **kwargs):
        """Instantiates an object of BaseModel
        Args:
            args (tuple)
            kwargs (dict)
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
                elif key == "updated_at" or key == "created_at":
                    date_obj = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, date_obj)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Prints a string rep of the object instant"""
        ret = "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            self.__dict__
        )
        return ret

    def save(self):
        """updates the public instance attribute
        updated_at with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """ returns a dictionary containing all
        keys/values of __dict__ of the instance"""
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict
