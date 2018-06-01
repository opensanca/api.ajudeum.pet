from datetime import date, datetime
from decimal import Decimal

from flask import json
from flask_sqlalchemy import DeclarativeMeta


class AlchemyJSONEncoder(json.JSONEncoder):

    def default(self, o):

        # check if object `o` is of custom declared model instance
        if isinstance(o.__class__, DeclarativeMeta):

            data = {}
            fields = o.__json__() if hasattr(o, '__json__') else dir(o)

            for field in [f for f in fields if not f.startswith('_') and f not in ['metadata', 'query', 'query_class']]:
                value = getattr(o, field)

                try:
                    if json.dumps(value):
                        data[field] = value

                except TypeError:
                    data[field] = None

            return data

        # check if object `o` is of Decimal instance
        elif isinstance(o, Decimal):
            return o.to_eng_string()

        # check if object `o` is of date instance
        elif isinstance(o, date):
            return o.isoformat()

        # rest of objects are handled by default JSONEncoder like `Datetime`, `UUID`, `Markdown` and various others
        return json.JSONEncoder.default(self, o)
