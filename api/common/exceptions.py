"""
Exceptions da API
"""
from .utils import HTTP_STATUS_CODES


class InvalidInput(Exception):
    """Exceção de entrada inválida."""
    status_code = HTTP_STATUS_CODES['BAD_REQUEST']

    def __init__(self, errors):
        Exception.__init__(self)
        self.errors = errors
