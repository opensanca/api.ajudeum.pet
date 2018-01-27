"""
    Schema para validação de dados de animais
"""
from marshmallow import Schema, fields


class AnimalSchema(Schema):
    """
        Classe responsavel pelo Schema de Animal do Marshmallow
    """
    name = fields.String(required=True)
    age = fields.Integer()
    breed = fields.List(fields.String())
    description = fields.String()
    arrived_date = fields.Date()
