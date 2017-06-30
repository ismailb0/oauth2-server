""" Defines the Client repository """

from models import GrantToken


class GrantTokenRepository:
    """ The repository for the grant_token model """

    @staticmethod
    def get(client_id, code):
        """ Query grant_token by client_id and code"""
        return Grant.query.filter_by(client_id=client_id, code=code).first()

    @staticmethod
    def save(client_id, code, request):
        """ Query grant_token by client_id and code"""
        expires = datetime.utcnow() + timedelta(seconds=100)
        grant = Grant(
            client_id=client_id,
            code=code['code'],
            redirect_uri=request.redirect_uri,
            _scopes=' '.join(request.scopes),
            user=get_current_user(),
            expires=expires
        )
        db.session.add(grant)
        db.session.commit()
        return grant
