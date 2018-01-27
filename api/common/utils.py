"""
Módulo de classes utilitárias
"""
import json
from functools import wraps


def json_result(wrapped):
    """ Decora uma função para retornar uma requisição no formato JSON"""
    @wraps(wrapped)
    def wrapper(*args, **kwargs):
        """ Repassa os argumetos da função original para o formatador JSON"""
        response = wrapped(*args, **kwargs)
        return json.dumps(response)
    return wrapper


HTTP_STATUS_CODES = {
    'OK': 200,
}
