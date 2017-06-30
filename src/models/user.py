"""
Define the User model
"""

from . import db
from .abc import BaseModel


class User(db.Model, BaseModel):
    """ The User model """
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), unique=True)

    def __init__(self, first_name, last_name, age=None):
        """ Create a new User """
        self.id = id
        self.username = username

    def to_dict(self):
        """ Return the User model as a python dictionary """
        return {
            'id': self.id,
            'username': self.username,
        }
