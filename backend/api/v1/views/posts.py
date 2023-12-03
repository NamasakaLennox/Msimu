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


@app_views.route('/posts/', strict_slashes=False, defaults={'post_id': None})
@app_views.route('/posts/<post_id>', strict_slashes=False)
def all_posts(post_id):
    """
    returns data for prediction
    """
    if post_id:
        post = storage.get(Post, post_id)
        if post:
            return post.to_dict()
        else:
            return jsonify({"error": "Not Found"})
    else:
        output = {}
        posts = storage.all(Post).values()
        for obj in posts:
            output[obj.id] = obj.to_dict()

        return (jsonify(output))

@app_views.route('/comments/<post_id>', strict_slashes=False)
def all_comments(post_id):
    """
    returns data for prediction
    """
    output = {}
    comments = storage.all(Comment).values()
    for comment in comments:
        if comment.post_id == post_id:
            output[comment.id] = comment.to_dict()

    if output == {}:
        return jsonify({"Message": "No comments found"})
    return (jsonify(output))
