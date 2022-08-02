#!/usr/bin/python3
"""Defines all common attributes/methods for other classes
"""
import uuid
import datetime


class BaseModel:
    """Base class for all models"""

    def __init__(self):
        """Create a new model"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
