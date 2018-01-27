from .utils import HTTP_STATUS_CODES


class InvalidInput(Exception):
    status_code = HTTP_STATUS_CODES['BAD_REQUEST']

    def __init__(self, errors):
        Exception.__init__(self)
        self.errors = errors
