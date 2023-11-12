#!/usr/bin/python3
"""
Defines a table for services storage
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Text
from sqlalchemy.orm import relationship


class Services(BaseModel, Base):
    """
    defines a services object and properties
    """
    __tablename__ = 'services'
    name = Column(String(128), nullable=False, unique=True)
    location_id = Column(String(60), ForeignKey('locations.id'), nullable=False)
