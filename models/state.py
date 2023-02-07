#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv
from os import environ


storage_engine = environ.get("HBNB_TYPE_STORAGE")


class State(BaseModel, Base):
    """ State class """
    if (storage_engine == 'db'):
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state" , cascade="delete")
    else:
        name = ""

    @property
    def cities(self):
        """Getters"""
        listes = []
        for city in models.storage.all(City).values():
            if city.state_id == self.id:
                listes.append(city)
        return listes
