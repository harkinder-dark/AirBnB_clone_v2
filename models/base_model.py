#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
from uuid import uuid4
from datetime import datetime
from sqlalchemy import DateTime
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from os import environ


storage_engine = environ.get("HBNB_TYPE_STORAGE")

if (storage_engine == "db"):
    Base = declarative_base()
else:
    Base = object

class BaseModel:
    """A base class for all hbnb models"""

    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            self.created_at = self.updated_at = datetime.utcnow()
        else:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key != "__class__":
                    setattr(self, key, value)
                else:
                    continue
        self.id = str(uuid4())

    def __str__(self):
        """Returns a string representation of the instance"""
        return '[{}] ({}) {}'.format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dic = self.__dict__.copy()
        dictionary = {}
        dictionary.update({'__class__':
                          self.__class__.__name__})
        for key in list(dic):
            if key in ('created_at', 'updated_at'):
                dictionary.update({key: getattr(self, key).isoformat()})
            elif key == "_sa_instance_state":
                dic.pop(key)
            else:
                dictionary.update({key: getattr(self, key)})
        return dictionary

    def delete(self):
        """delete method"""
        from models import storage
        key = "{}.{}".format(type(self).__name__, self.id)
        del storage.__objects[key]
