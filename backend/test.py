#!/usr/bin/python3
"""
test if everything is working fine
"""
from models.comments import Comment
from models.location_services import LocationService
from models.locations import Location
from models.posts import Post
from models.prediction import Prediction
from models.services import Service
from models.users import User
from models.weather_data import WeatherData
from models import storage

"""
new_user = User(first_name="John", last_name="Doe", username="johndoe",
                email="john@example.com", password="password123",
                phonenumber="123456789", location_id="some_location_id",
                image="path/to/image")
print(new_user)
new_user.save()
"""

print("----reload_all----")
all_obj = storage.all().values()
for obj in all_obj:
    print(obj)

print("---new-all---")
