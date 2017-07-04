"""
Define the REST verbs relative to the token
"""

from flask.ext.restful import Resource
from flask.json import jsonify

class TokenResource(Resource):
    """ Verbs relative to the token """
    @staticmethod
    @oauth.token_handler
    def post():
        return None
