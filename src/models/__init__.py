from flask.ext.sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from .user import User
from .client import Client
