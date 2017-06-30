"""
Define the REST verbs relative to the users
"""

from flask.ext.restful import Resource
from flask.json import jsonify

from repositories import UserRepository

class UserResource(Resource):
    """ Verbs relative to the user """
    @staticmethod
    def get(id):
        """ Return the first user that matches the given username """
        user_repository = UserRepository()
        user = user_repository.get(id)
        return user.to_dict()
