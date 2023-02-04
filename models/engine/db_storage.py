#!/usr/bin/python3
"""databases storage file"""


from sqlalchemy import create_engine
from os import getenv
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy.orm import scoped_session


HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')


class DBStorage:
    """database class"""
    __engine = None
    __session = None

    def __init__(self):
        """initialisation function"""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}"
                                      .format(HBNB_MYSQL_USER,
                                              HBNB_MYSQL_PWD,
                                              HBNB_MYSQL_HOST,
                                              HBNB_MYSQL_DB),
                                      pool_pre_ping=True)
        if HBNB_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """all methods"""
        cls_dict = {}   
        objs = [User, State, City, Amenity, Place, Review]
        if cls:
            for obj in self.__session.query(cls).all():
                key = "{}.{}".format(cls.__name__, obj.id)
                obj.to_dict()
                cls_dict.update({key: obj})
        else:
            for obj in objs:
                for row in self.__session.query(obj).all():
                    key = "{}.{}".format(obj.__name__, row.id)
                    row.to_dict()
                    cls_dict.update({key: obj})
        return cls_dict

    def new(self, obj):
        """create new instances"""
        self.__session.add(obj)

    def save(self):
        """saving"""
        self.__session.commit()

    def delete(self, obj=None):
        """deleting"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloading..."""
        from sqlalchemy.orm import sessionmaker
        Base.metadata.create_all(self.__engine)
        session_ = sessionmaker(bind=self.__engine,
                                expire_on_commit=False)
        Session = scoped_session(session_)
        self.__session = Session()

    def close(self):
        """Close the working SQLAlchemy session."""
        self.__session.__class__.close(self.__session)
        self.reload()
