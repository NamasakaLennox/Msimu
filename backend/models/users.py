#!/usr/bin/python3
"""
Defines a user for the models
"""
from models.basemodel import BaseModel, Base
from sqlalchemy import Column, ForeignKey, String
from hashlib import md5


class User(BaseModel, Base):
    """
    defines a user object and properties
    """
    __tablename__ = 'users'
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    username = Column(String(128), nullable=False)
    email = Column(String(128), nullable=True)
    password = Column(String(128), nullable=False)
    phonenumber = Column(String(128), nullable=False)
    location_id = Column(String(60), ForeignKey('locations.id'), nullable=False)
    image = Column(String(128), nullable=False)

    def __init__(self, *args, **kwargs):
        """
        constructor method for user class
        """
        super().__init__(*args, **kwargs)

    def __setattr__(self, name, value):
        """
        sets a password with md5 encryption
        """
        if name == "password":
            value = md5(value.encode()).hexdigest()
        super().__setattr__(name, value)

    def check_password(self, password):
        """
        checks if password matches the stored hash value
        """
        return self.password == md5(password.encode()).hexdigest()
