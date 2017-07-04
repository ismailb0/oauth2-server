"""
Define the REST verbs relative to the authorize resource
"""

from flask.ext.restful import Resource
from flask.json import jsonify
from flask import render_template, request
from repositories import ClientRepository

class AuthorizeResource(Resource):
    """ Verbs relative to the authorize resource """

    @oauth.authorize_handler
    def get(*args, **kwargs):
        client_id = kwargs.get('client_id')
        client = ClientRepository.get(client_id=client_id)
        kwargs['client'] = client
        return render_template('oauthorize.html', **kwargs)

    @oauth.authorize_handler
    def post():
        confirm = request.form.get('confirm', 'no')
        return confirm == 'yes'
