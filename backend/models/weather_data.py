#!/usr/bin/python3
"""
Defines a table for weather data storage
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Text
from sqlalchemy.orm import relationship


class WeatherData(BaseModel, Base):
    """
    defines a weather_data object and properties
    """
    __tablename__ = 'weather_data'
    location_id = Column(String(60), ForeignKey('locations.id'), nullable=False)
    rainfall = Column(Float(5), nullable=True)
