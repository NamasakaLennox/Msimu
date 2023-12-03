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


@app_views.route('/posts/', strict_slashes=False, defaults={'post_id': None})
@app_views.route('/posts/<post_id>', strict_slashes=False)
@token_required
def all_posts(current_user, post_id):
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

@app_views.route('/posts/', strict_slashes=False, methods=["POST"])
@token_required
def create_post(current_user):
    props = request.get_json()
    if type(props) != dict:
        return (jsonify({"Error": "cannot create post"}))

    if props.get("text") == None:
        return (jsonify({"Message": "Post can't be empty"}))

    new_post = Post(user_id=current_user.id, post_text=props.get("text"), comment_image=props.get("image"), likes=0)
    new_post.save()

    return (jsonify({"Message": "Post Created", "post": new_post.to_dict()}))


@app_views.route('/comments/<post_id>', strict_slashes=False)
@token_required
def all_comments(current_user, post_id):
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

@app_views.route('/comments/<post_id>', strict_slashes=False, methods=["POST"])
@token_required
def create_comment(current_user, post_id):
    props = request.get_json()
    if type(props) != dict:
        return (jsonify({"Error": "cannot create post"}))
    if not props.get("post_id"):
        return (jsonify({"Message": "Please provide the post id"}))

    new_comment = Comment(user_id=current_user.id, post_id=props.get("post_id"), comment_text=props.get("text"), comment_image=props.get("image"), likes=0)
    new_comment.save()

    return (jsonify({"Message": "Comment Created", "comment": new_comment.to_dict()}))
