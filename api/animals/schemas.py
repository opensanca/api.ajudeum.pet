from marshmallow import Schema, fields


# pylint: disable=too-few-public-methods
class AnimalSchema(Schema):
    name = fields.String(required=True)
    age = fields.Integer()
    breed = fields.String()
    description = fields.String()
    arrived_date = fields.Date()
