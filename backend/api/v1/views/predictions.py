#!/usr/bin/python3
"""
handles prediction routes
"""
from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.comments import Comment
from models.location_services import LocationService
from models.locations import Location
from models.posts import Post
from models.prediction import Prediction
from models.services import Service
from models.users import User
from models.weather_data import WeatherData


classes = {"Comment": Comment, "LocationService": LocationService,
           "Location": Location, "Post": Post, "Prediction": Prediction,
           "Service": Service, "User": User, "WeatherData": WeatherData}


@app_views.route('/prediction/', strict_slashes=False)
def all_prediction():
    """
    returns data for prediction
    """
    output = {}
    prediction = storage.all(Prediction).values()
    for obj in prediction:
        output[obj.location_id] = obj.to_dict()
    print(output)

    return (jsonify(output))
