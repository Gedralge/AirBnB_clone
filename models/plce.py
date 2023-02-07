#!/usr/bin/python3
"""Place Module for HBNB project"""
from models.base_model import BaseModel


class place(BaseModel):
    """ A place to stay """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guests = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amentity_ids = []
    
