"""
Define the REST verbs relative to the authorize resource
"""

from flask.ext.restful import Resource
from flask.json import jsonify
from flask import render_template, request
from repositories import ClientRepository, UserRepository
from server import oauth
import logging

class AuthorizeResource(Resource):
    """ Verbs relative to the authorize resource """

    @staticmethod
    def get(*args, **kwargs):
        client_id = request.args.get('client_id')
        client = ClientRepository.get(client_id=client_id)
        user = UserRepository.get(id=client.user_id)
        kwargs['client'] = client
        kwargs['user'] = user
        return render_template('oauthorize.html', **kwargs)

    @staticmethod
    def post():
        confirm = request.form.get('confirm', 'no')
        return confirm == 'yes'
