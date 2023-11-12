#!/usr/bin/python3
"""
Defines a table for services storage
"""
from models.basemodel import BaseModel, Base
from sqlalchemy import Column, String, Text
from sqlalchemy.orm import relationship


class Service(BaseModel, Base):
    """
    defines a services object and properties
    """
    __tablename__ = 'services'
    name = Column(String(128), nullable=False, unique=True)
    description = Column(Text, nullable=False)
