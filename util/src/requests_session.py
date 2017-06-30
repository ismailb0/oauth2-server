import requests


def get_new_requests_session():
    """Return a new request session."""
    s = requests.Session()
    http_handler = requests.adapters.HTTPAdapter(max_retries=5)
    https_handler = requests.adapters.HTTPAdapter(max_retries=5)
    s.mount('http://', http_handler)
    s.mount('https://', https_handler)

    return s
