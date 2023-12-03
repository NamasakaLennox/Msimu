#!/usr/bin/python3
"""
The BaseModel module where all classes inherit it's properties
"""
from datetime import datetime
from os import getenv
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from uuid import uuid4

time = "%Y-%m-%dT%H:%M:%S.%f"  # format for time

Base = declarative_base()

class BaseModel:
    """
    The base class for all tables
    """
    id = Column(String(60), primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """
        constructor method for the class
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)

            if kwargs.get("created_at", None) and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], time)
            else:
                self.created_at = datetime.utcnow()

            if kwargs.get("updated_at", None) and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], time)
            else:
                self.updated_at = datetime.utcnow()

            if kwargs.get("id", None) is None:
                self.id = str(uuid4())

        else:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at

    def __str__(self):
        """
        Returns a string representation of a class object
        """
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)

    def save(self):
        """
        adds the new object to the database
        """
        from models import storage
        self.updated_at = datetime.utcnow()
        storage.new(self)
        storage.save()

    def to_dict(self, save_fs=None):
        """
        returns a dictionary representation of the class object
        """
        new = self.__dict__.copy()
        if "created_at" in new:
            new["created_at"] = new["created_at"].strftime(time)
        if "updated_at" in new:
            new["updated_at"] = new["updated_at"].strftime(time)

        if "_sa_instance_state" in new:
            del new["_sa_instance_state"]
        if save_fs is None:
            if "password" in new:
                del new["password"]

        return new

    def delete(self):
        """
        removes the current instance from database
        """
        from models import storage
        storage.delete(self)

    def filter_by(self, **kwargs):
        """filter by given arguments"""
        return (storage.filter_by(self, **kwargs))
