"""
Method to decorate the server to handle exceptions
"""
import traceback
import logging
import re
from flask import jsonify
from requests.exceptions import ConnectionError
from werkzeug.exceptions import BadRequest

import config
from errors import CustomException
# Leave this import even if unused, as it is important to have the SMTP handler
# for logs
import smtp_logging_config


def add_error_handlers(server):
    # This config is necessary to propagate errors in blueprints to the globar error handler
    server.config['PROPAGATE_EXCEPTIONS'] = True

    @server.errorhandler(CustomException)
    def handle_custom_errors(err):
        status_code = err.status_code
        if status_code < 500:
            logging.error(err, exc_info=True)
        else:
            logging.critical(err, exc_info=True)
        response = {
            'message': err.message,
            'value': err.value,
            'key': err.key
        }
        if config.DEBUG:
            response['traceback'] = traceback.format_exc()
            response['stack'] = [config.APPLICATION_ROOT] if err.stack is None else err.stack + [config.APPLICATION_ROOT]
        return jsonify(response), status_code

    @server.errorhandler(BadRequest)
    def handle_bad_requests(err):
        logging.error(err, exc_info=True)

        try:
            service = re.search('http://[^/]+(/[^/]+)', err.request.url).groups()[0]
        except:
            service = '/??'

        response = {
            'message': err.get_description(),
            'value': None,
            'key': 'INPUT_ERROR',
        }
        if config.DEBUG:
            response['traceback'] = traceback.format_exc()
            response['stack'] = [service]
        return jsonify(response), 400

    @server.errorhandler(ConnectionError)
    def handle_connection_errors(err):
        logging.critical(err, exc_info=True)
        response = {
            'message': 'Error requesting URL',
            'value': err.request.url,
            'key': 'HTTP_CONNECTION_EXCEPTION'
        }
        if config.DEBUG:
            try:
                service = re.search('http://[^/]+(/[^/]+)', err.request.url).groups()[0]
            except:
                service = '/??'
            response['traceback'] = traceback.format_exc()
            response['stack'] = [service]
        return jsonify(response), 503

    @server.errorhandler(Exception)
    def handle_exceptions(err):
        logging.critical(err, exc_info=True)
        response = {
            'key': 'INTERNAL_SERVER_ERROR'
        }
        if config.DEBUG:
            response['error_class'] = type(err).__name__
            response['message'] = str(err)
            response['traceback'] = traceback.format_exc()
        return jsonify(response), 500
