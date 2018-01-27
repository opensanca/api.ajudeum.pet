"""
Módulo para classes de persistência
"""
from datetime import datetime
from mongoengine import Document, StringField, IntField, ListField, DateTimeField


# pylint: disable=too-few-public-methods
class Animal(Document):
    """Dados cadastrais do animal"""
    name = StringField(required=True)
    age = IntField()
    breed = ListField()
    arrived_date = DateTimeField(default=datetime.now())
    description = StringField()

    def __init__(self, name, age, breed, arrived_date, description, *args, **kwargs): # pylint: disable=too-many-arguments
        super(Animal, self).__init__(*args, **kwargs)
        self.name = name
        self.age = age
        self.breed = breed
        self.arrived_date = arrived_date
        self.description = description
