#!/usr/bin/python3
"""Review model for the HBNB project"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review class to store review information """
    place_id = ""
    user_id = ""
    text = ""
