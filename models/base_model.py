#!/usr/bin/python3
"""This model contains the base class
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """
    base class
    """
    def __init__(self, *args, **kwargs):

        if kwargs:
            del kwargs["__class__"]
            for key, value in kwargs.items():
                if key in ("cretaed_at", "updated_at"):
                    setattr(self, key, datetime.strptime(value,
                            "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, key, value)
        else:

            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        diction = {}
        diction["__class__"] = self.__class__.__name__

        for key, value in self.__dict__.items():
            if isinstance(value, datetime):
                diction[key] = value.isoformat()
            else:
                diction[key] = value
        return diction

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)
