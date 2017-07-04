"""
Defines the blueprint for the token
"""
from flask import Blueprint
from flask.ext.restful import Api

from resources import TokenResource


TOKEN_BLUEPRINT = Blueprint('token', __name__)
Api(TOKEN_BLUEPRINT).add_resource(TokenResource, '/token')
