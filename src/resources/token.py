"""
Define the REST verbs relative to the token
"""

from flask.ext.restful import Resource
from flask.json import jsonify
from server import oauth

class TokenResource(Resource):
    """ Verbs relative to the token """
    @staticmethod
    @oauth.token_handler
    def post():
        return None
