import json
from functools import wraps


def json_result(wrapped):
    @wraps(wrapped)
    def wrapper(*args, **kwargs):
        response = wrapped(*args, **kwargs)
        return json.dumps(response)
    return wrapper


HTTP_STATUS_CODES = {
    'OK': 200,
    'BAD_REQUEST': 400,
}
