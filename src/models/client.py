"""
Define the Client model
"""

from . import db
from .abc import BaseModel


class Client(db.Model):
    name = db.Column(db.String(40))
    description = db.Column(db.String(400))
    user_id = db.Column(db.ForeignKey('user.id'))
    user = db.relationship('User')
    client_id = db.Column(db.String(40), primary_key=True)
    client_secret = db.Column(db.String(55), unique=True, index=True,
                              nullable=False)
    is_confidential = db.Column(db.Boolean)
    _redirect_uris = db.Column(db.Text)
    _default_scopes = db.Column(db.Text)

    def __init__(
        self,
        name,
        description,
        user_id,
        client_id,
        client_secret,
        is_confidential,
        _redirect_uris,
        _default_scopes
        ):
        """ Create a new Client """

        self.name = name
        self.description = description
        self.user_id = user_id
        self.client_id = client_id
        self.client_secret = client_secret
        self.is_confidential = is_confidential
        self._redirect_uris = _redirect_uris
        self._default_scopes = _default_scopes

    @property
    def client_type(self):
        if self.is_confidential:
            return 'confidential'
        return 'public'

    @property
    def redirect_uris(self):
        if self._redirect_uris:
            return self._redirect_uris.split()
        return []

    @property
    def default_redirect_uri(self):
        return self.redirect_uris[0]

    @property
    def default_scopes(self):
        if self._default_scopes:
            return self._default_scopes.split()
        return []

    def to_dict(self):
        """ Return a dict representation of the Client model """
        return {
            'name': self.name,
            'description': self.description,
            'user_id': self.user_id,
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'is_confidential': self.client_type,
            '_redirect_uris': self.redirect_uris,
            '_default_scopes': self.default_scopes,
        }
