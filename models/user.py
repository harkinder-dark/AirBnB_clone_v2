#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import environ


storage_engine = environ.get("HBNB_TYPE_STORAGE")


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    if (storage_engine == 'db'):
        __tablename__ = "users"
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128))
        last_name = Column(String(128))
        places = relationship("Place", backref="user", cascade="delete")
        reviews = relationship("Review", backref="user", cascade="delete")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
