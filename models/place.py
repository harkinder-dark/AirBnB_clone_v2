#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy import Integer, Float, Table
from os import environ
import models


storage_engine = environ.get("HBNB_TYPE_STORAGE")
if storage_engine == "db":
    place_amenity = Table("place_amenity", Base.metadata,
                          Column('place_id', String(60),
                                 ForeignKey("places.id"),
                                 primary_key=True,
                                 nullable=False),
                          Column('amenity_id', String(60),
                                 ForeignKey("amenities.id"),
                                 primary_key=True,
                                 nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    if (storage_engine == "db"):
        city_id = Column(String(60), nullable=False, ForeignKey("cities.id"))
        user_id = Column(String(60), nullable=False, ForeignKey("users.id"))
        name = Column(String(128), nullable=False)
        description = Column(String(1024))
        number_rooms = Column(Integer, default=0)
        number_bathrooms = Column(Integer, default=0)
        max_guest = Column(Integer, default=0)
        price_by_night = Column(Integer, default=0)
        latitude = Column(Float)
        longitude = Column(Float)
        reviews = relationship("Review", back_populates="place", cascade="delete")
        amenities = relationship("Amenity", secondary=place_amenity,
                                 back_populates="place_amenities",
                                 viewonly=False)
        amenity_ids = []
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

    @property
    def reviews(self):
        """Get a list of all linked Reviews."""
        review_list = []
        for review in list(models.storage.all(Review).values()):
            if review.place_id == self.id:
                review_list.append(review)
        return review_list
    
    @property
    def amenities(self):
        """Get/set linked Amenities."""
        amenity_list = []
        for amenity in list(models.storage.all(Amenity).values()):
            if amenity.id in self.amenity_ids:
                amenity_list.append(amenity)
        return amenity_list

    @amenities.setter
    def amenities(self, value):
        if type(value) == Amenity:
            self.amenity_ids.append(value.id)
