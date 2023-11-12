#!/usr/bin/python3
"""
Defines a table for prediction storage
"""
from models.basemodel import BaseModel, Base
from sqlalchemy import Column, Float, ForeignKey, String, Text
from sqlalchemy.orm import relationship


class Prediction(BaseModel, Base):
    """
    defines a prediction object and properties
    """
    __tablename__ = 'predictions'
    location_id = Column(String(60), ForeignKey('locations.id'), nullable=False)
    value = Column(Float(5), nullable=True)
