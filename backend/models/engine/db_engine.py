#!/usr/bin/python3
"""
Handles database mapping and database operations
"""
from models.basemodel import BaseModel, Base
from models.comments import Comment
from models.location_services import LocationService
from models.locations import Location
from models.posts import Post
from models.prediction import Prediction
from models.services import Service
from models.users import User
from models.weather_data import WeatherData
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

classes = {"Comment": Comment, "LocationService": LocationService,
           "Location": Location, "Post": Post, "Prediction": Prediction,
           "Service": Service, "User": User, "WeatherData": WeatherData}


class DBStorage:
    """
    handles MySQL database operations
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        Constructor method for the class object
        """
        MSIMU_ENV = getenv('MSIMU_ENV')
        MSIMU_MYSQL_USER = getenv('MSIMU_MYSQL_USER')
        MSIMU_MYSQL_PORT = getenv('MSIMU_MYSQL_PORT')
        MSIMU_MYSQL_DB = getenv('MSIMU_MYSQL_DB')
        MSIMU_MYSQL_HOST = getenv('MSIMU_MYSQL_HOST')
        MSIMU_MYSQL_PWD = getenv('MSIMU_MYSQL_PWD')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(MSIMU_MYSQL_USER,
                                             MSIMU_MYSQL_PWD,
                                             MSIMU_MYSQL_HOST,
                                             MSIMU_MYSQL_DB),
                                      pool_pre_ping=True)

        if MSIMU_ENV == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        returns all class objects in the database
        """
        new_dict = {}
        for item in classes:
            if cls is None or cls is item or cls is classes[item]:
                objs = self.__session.query(classes[item]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj

        return (new_dict)

    def new(self, obj):
        """
        add a new object to current database session
        """
        if obj:
            self.__session.add(obj)

    def save(self):
        """
        saves the current session changes to the database
        """
        if obj:
            self.__session.commit()

    def delete(self, obj=None):
        """
        deletes an object from the database
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
        fetches data from the database
        """
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session)
        self.__session = Session

    def get(self, cls, id):
        """
        gets an object given a class and id
        """
        from models import storage

        if cls not in classes.values():
            return None
        all_cls = storage.all(cls)

        for value in all_cls.values():
            if value.id == id:
                return value

    def count(self, cls=None):
        """counts the number of items in classes"""
        from models import storage
        count = len(storage.all(cls))
        return count

    def close(self):
        """
        removes the current session
        """
        self.__session.remove()

    def session(self):
        """
        returns the current session
        """
        return self.__session
