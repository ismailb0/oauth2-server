""" Defines the User repository """

from models import User


class UserRepository:
    """ The repository for the user model """

    @oauth.usergetter
    def get(id):
        """ Query users by username """
        return User.query.filter_by(id=id).first()
