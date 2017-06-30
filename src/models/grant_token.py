"""
Define the GrantToken model
"""

from . import db
from .abc import BaseModel


class GrantToken(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.Integer, db.ForeignKey('user.id', ondelete='CASCADE')
    )
    user = db.relationship('User')
    client_id = db.Column(
        db.String(40), db.ForeignKey('client.client_id'),
        nullable=False,
    )
    client = db.relationship('Client')
    code = db.Column(db.String(255), index=True, nullable=False)
    redirect_uri = db.Column(db.String(255))
    expires = db.Column(db.DateTime)
    _scopes = db.Column(db.Text)

    def __init__(
        self,
        id,
        user_id,
        client_id,
        code,
        redirect_uri,
        expires
        ):
        """ Create a new GrantToken """

        self.id = id
        self.user_id = user_id
        self.client_id = client_id
        self.code = code
        self.redirect_uri = redirect_uri
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
        """ Return a dict representation of the GrantToken model """
        return {
            'id': self.id,
            'user_id': self.user_id,
            'client_id': self.client_id,
            'code': self.code,
            'redirect_uri': self.redirect_uri,
            'expires': self.expires,
            'scopes': self.scopes,
        }
