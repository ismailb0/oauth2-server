"""
Define the Token model
"""

from . import db
from .abc import BaseModel


class Token(db.Model):
    """ The Token model """

    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(
        db.String(40), db.ForeignKey('client.client_id'),
        nullable=False,
    )
    client = db.relationship('Client')

    user_id = db.Column(
        db.Integer, db.ForeignKey('user.id')
    )
    user = db.relationship('User')

    # currently only bearer is supported
    token_type = db.Column(db.String(40))

    access_token = db.Column(db.String(255), unique=True)
    refresh_token = db.Column(db.String(255), unique=True)
    expires = db.Column(db.DateTime)
    _scopes = db.Column(db.Text)

    def __init__(self, first_name, last_name, age=None):
        """ Create a new User """
        self.id = id
        self.client_id = client_id
        self.user_id = user_id
        self.token_type = token_type
        self.access_token = access_token
        self.refresh_token = refresh_token
        self.expires = expires
        self._scopes = _scopes

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return self

    @property
    def scopes(self):
        if self._scopes:
            return self._scopes.split()
        return []

    def to_dict(self):
        """ Return the Token model as a python dictionary """
        return {
            'id': self.id,
            'client_id': self.client_id,
            'user_id': self.user_id,
            'token_type': self.token_type,
            'access_token': self.access_token,
            'refresh_token': self.refresh_token,
            'expires': self.expires,
            'scopes': self.scopes
        }
