"""
initializes the database
"""
from models.basemodel import BaseModel
from models.comments import Comment
from models.engine.db_storage import DBStorage
from models.location_services import LocationService
from models.locations import Location
from models.posts import Post
from models.prediction import Prediction
from models.services import Service
from models.users import User
from models.weather_data import WeatherData

storage = DBStorage()
storage.reload()
