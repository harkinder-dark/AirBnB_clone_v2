#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import environ


storage_engine = environ.get("HBNB_TYPE_STORAGE")


class Review(BaseModel):
    """ Review classto store review information """
    if (storage_engine == 'db'):
        __tablename__ = "reviews"
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), nullable=False, ForeignKey("places.id"))
        user_id = Column(String(60), nullable=False, ForeignKey("users.id"))
    else:
        place_id = ""
        user_id = ""
        text = ""
