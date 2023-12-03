#!/usr/bin/python3
"""
defines the blueprints
"""
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

from api.v1.views.index import *
from api.v1.views.predictions import *
from api.v1.views.posts import *
