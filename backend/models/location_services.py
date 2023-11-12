#!/usr/bin/python3
"""
Defines a table for location_services storage
"""
from models.basemodel import BaseModel, Base
from sqlalchemy import Column,ForeignKey, String, Text
from sqlalchemy.orm import relationship


class LocationService(BaseModel, Base):
    """
    defines a location_service object and properties
    """
    __tablename__ = 'location_services'
    service_id = Column(String(60), ForeignKey('services.id'), nullable=False)
    location_id = Column(String(60), ForeignKey('locations.id'), nullable=False)
