#!/usr/bin/python3
"""
test if everything is working fine
"""
from models import storage
from models.comments import Comment
from models.location_services import LocationService
from models.locations import Location
from models.posts import Post
from models.prediction import Prediction
from models.services import Service
from models.users import User
from models.weather_data import WeatherData

print("----reload_all----")
all_obj = storage.all(obj).values()
for obj in all_obj:
    print(obj)

print("---new-all---")
