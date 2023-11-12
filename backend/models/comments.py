#!/usr/bin/python3
"""
Defines a table for comments
"""
from models.basemodel import BaseModel, Base
from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship


class Comment(BaseModel, Base):
    """
    defines a comment object and properties
    """
    __tablename__ = 'comments'
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    post_id = Column(String(60), ForeignKey('posts.id'), nullable=False)
    comment_text = Column(Text, nullable=False)
    comment_image = Column(String(128), nullable=True)
    likes = Column(Integer, nullable=False, default=0)
