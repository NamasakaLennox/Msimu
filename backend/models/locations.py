#!/usr/bin/python3
"""
Defines a table for location storage
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Text
from sqlalchemy.orm import relationship


class Location(BaseModel, Base):
    """
    defines a prediction object and properties
    """
    __tablename__ = 'locations'
    name = Column(String(128), nullable=False, unique=True)
    latitude = Column(String(128), nullable=False)
    longitude = Column(String(128), nullable=False)
