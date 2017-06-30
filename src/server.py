from flask import Flask
from flask.blueprints import Blueprint
from flask.ext.cors import CORS
from raven.contrib.flask import Sentry
from flask_oauthlib.provider import OAuth2Provider

import config
from models import db

# config your API specs
# you can define multiple specs in the case your api has multiple versions
# ommit configs to get the default (all views exposed in /spec url)
# rule_filter is a callable that receives "Rule" object and
#   returns a boolean to filter in only desired views

server = Flask(__name__)
oauth = OAuth2Provider(server)

if config.SENTRY_DSN is not None:
    sentry = Sentry(server, dsn=config.SENTRY_DSN)
server.debug = config.DEBUG
server.config['SQLALCHEMY_DATABASE_URI'] = config.DB_URI
CORS(server, resources={r"/*": {"origins": "*"}}, headers=['Content-Type', 'X-Requested-With', 'Authorization'])
db.init_app(server)
db.app = server

import route
for blueprint in vars(route).values():
    if isinstance(blueprint, Blueprint):
        server.register_blueprint(blueprint, url_prefix=config.APPLICATION_ROOT)

from common.blueprint import common_blueprint
server.register_blueprint(common_blueprint, url_prefix=config.APPLICATION_ROOT)

from common.blueprint import get_status_blueprint
server.register_blueprint(get_status_blueprint(checking_api='OAUTH2_SERVER_URL', checkDatabase=True), url_prefix=config.APPLICATION_ROOT)

if __name__ == '__main__':
    server.run(host=config.HOST, port=config.PORT)
