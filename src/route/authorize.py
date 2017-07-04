"""
Defines the blueprint for the authorize
"""
from flask import Blueprint
from flask.ext.restful import Api

from resources import AuthorizeResource


AUTHORIZE_BLUEPRINT = Blueprint('authorize', __name__)
Api(AUTHORIZE_BLUEPRINT).add_resource(AuthorizeResource, '/authorize')
