import logging
import os

DEBUG = True if os.getenv('DEBUG_MODE') == 'True' else False
APPLICATION_ROOT = os.getenv('OAUTH2_SERVER_APPLICATION_ROOT', '/oauth2-server')
HOST = os.getenv('OAUTH2_SERVER_HOST', '0.0.0.0')
PORT = int(os.getenv('OAUTH2_SERVER_PORT', '5000'))
WORKER_COUNT = os.getenv('OAUTH2_SERVER_WORKER_COUNT', 1)

# Config for sentry
SENTRY_DSN = os.getenv('SENTRY_DSN', None)

DB_CONTAINER = os.getenv('OAUTH2_SERVER_DB_CONTAINER', 'DB')
DATABASE = {
    'type': 'mysql',
    'user': os.getenv('OAUTH2_SERVER_DB_USER'),
    'pw': os.getenv('OAUTH2_SERVER_DB_PW', ''),
    'host': os.getenv('OAUTH2_SERVER_DB_HOST', os.getenv('%s_PORT_3306_TCP_ADDR' % DB_CONTAINER)),
    'port': os.getenv('OAUTH2_SERVER_DB_PORT', os.getenv('%s_PORT_3306_TCP_PORT' % DB_CONTAINER)),
    'db': os.getenv('OAUTH2_SERVER_DB_NAME', os.getenv('%s_ENV_MYSQL_DATABASE' % DB_CONTAINER)),
}
DB_URI = '%(type)s://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % DATABASE

logging.basicConfig(
    filename=os.getenv('SERVICE_LOG', 'server.log'),
    level=logging.DEBUG,
    format='%(levelname)s: %(asctime)s pid:%(process)s module:%(module)s %(message)s',
    datefmt='%d/%m/%y %H:%M:%S',
)
