#!/usr/bin/python3
"""
Defines a table for posts
"""
from models.basemodel import BaseModel, Base
from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship


class Post(BaseModel, Base):
    """
    defines a post object and properties
    """
    __tablename__ = 'posts'
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    post_text = Column(Text, nullable=False)
    comment_image = Column(String(128), nullable=True)
    likes = Column(Integer, nullable=False, default=0)
