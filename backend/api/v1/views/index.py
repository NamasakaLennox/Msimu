#!/usr/bin/python3
"""
this exposes the default public routes
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

@app_views.route('/', strict_slashes=False)
def available():
    """
    returns available routes
    """
    public_get = ["/status/", "stats"]
    auth_get = []
    auth_post = []
    auth_put = []
    auth_delete = []

    out = {"public_routes": {"get": public_get},
           "auth_required": {"get": auth_get,
                             "post": auth_post,
                             "put": auth_put,
                             "delete": auth_delete}
           }

    return jsonify(out)

@app_views.route('/status', strict_slashes=False)
def status():
    """
    returns ok if app is working
    """
    return jsonify({"status": "OK"})

@app_views.route('stats', strict_slashes=False)
def stats():
    """
    provides a statistics of the items available in database
    """
    values = classes.values()
    keys = classes.keys()

    out = {}
    for key, value in zip(keys, values):
        count = storage.count(value)
        out[key] == count

    return jsonify(out)
