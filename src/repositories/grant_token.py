""" Defines the GrantToken repository """

from models import GrantToken
from services import current_user


class GrantTokenRepository:
    """ The repository for the grant_token model """

    @oauth.grantgetter
    def get(client_id, code):
        """ Query grant_token by client_id and code"""
        return Grant.query.filter_by(client_id=client_id, code=code).first()

    @oauth.grantsetter
    def save(client_id, code, request):
        """ Save grant_token by client_id and code"""
        expires = datetime.utcnow() + timedelta(seconds=100)
        grant = Grant(
            client_id=client_id,
            code=code['code'],
            redirect_uri=request.redirect_uri,
            _scopes=' '.join(request.scopes),
            user=current_user(),
            expires=expires
        )
        db.session.add(grant)
        db.session.commit()
        return grant
