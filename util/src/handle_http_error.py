import json
import re
from errors import CustomException


def handle_http_error(response, service=None, value=None):
    if response.status_code >= 400:
        try:
            error = json.loads(response.text)

            exception = CustomException(
                message=error.get('message'),
                value=error.get('value'),
                key=error.get('key'),
                stack=error.get('stack'),
                status_code=response.status_code,
            )
        except Exception:
            try:
                service = re.search('http:\/\/[^\/]+(\/[^\/]+)', response.url).groups()[0]
            except:
                service = '/??'
            exception = CustomException(
                message='Error status >=400 but error content was not json',
                value={'text': response.text, 'url': response.url},
                key='UNDEFINED_EXCEPTION',
                status_code=response.status_code,
                stack=[service],
            )
        raise exception
