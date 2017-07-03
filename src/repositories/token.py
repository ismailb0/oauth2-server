""" Defines the Token repository """

from models import Token
from datetime import datetime, timedelta


class TokenRepository:
    """ The repository for the token model """

    @oauth.tokengetter
    def load_token(access_token=None):
        """ Query token by access_token"""
        if access_token:
            return Token.query.filter_by(access_token=access_token).first()

    @oauth.tokensetter
    def save_token(token, request):
        """ Save token by token and request"""
        tokens = Token.query.filter_by(client_id=request.client.client_id,
                                     user_id=request.user.id)
        # make sure that every client has only one token connected to a user
        for t in tokens:
            db.session.delete(t)

        expires_in = token.get('expires_in')
        expires = datetime.utcnow() + timedelta(seconds=expires_in)

        token = Token(
            access_token=token['access_token'],
            refresh_token=token['refresh_token'],
            token_type=token['token_type'],
            _scopes=token['scope'],
            expires=expires,
            client_id=request.client.client_id,
            user_id=request.user.id,
        )
        db.session.add(token)
        db.session.commit()
        return token
