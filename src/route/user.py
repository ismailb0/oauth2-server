"""
Defines the blueprint for the user
"""
from flask import Blueprint
from flask.ext.restful import Api

from resources import UserResource


USER_BLUEPRINT = Blueprint('user', __name__)
Api(USER_BLUEPRINT).add_resource(UserResource, '/user/<int:id>')
