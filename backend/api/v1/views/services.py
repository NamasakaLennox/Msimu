#!/usr/bin/python3
"""
handles prediction routes
"""
from api.v1.views import app_views
from flask import jsonify, request
from models import storage
from models.comments import Comment
from models.location_services import LocationService
from models.locations import Location
from models.posts import Post
from models.prediction import Prediction
from models.services import Service
from models.users import User
from models.weather_data import WeatherData
from api.v1.auth import token_required


classes = {"Comment": Comment, "LocationService": LocationService,
           "Location": Location, "Post": Post, "Prediction": Prediction,
           "Service": Service, "User": User, "WeatherData": WeatherData}


@app_views.route('/services/', strict_slashes=False, defaults={'service_id': None})
@app_views.route('/services/<service_id>', strict_slashes=False)
@token_required
def all_services(current_user, service_id):
    """
    returns data for prediction
    """
    if service_id:
        service = storage.get(Service, service_id)
        if service:
            return service.to_dict()
        else:
            return jsonify({"error": "Not Found"})
    else:
        output = {}
        services = storage.all(Service).values()
        for obj in services:
            output[obj.id] = obj.to_dict()

        return (jsonify(output))