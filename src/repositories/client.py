""" Defines the Client repository """

from models import Client
from server import oauth


class ClientRepository:
    """ The repository for the client model """

    @oauth.clientgetter
    def get(client_id):
        """ Query client by client_id """
        return Client.query.filter_by(client_id=client_id).first()
