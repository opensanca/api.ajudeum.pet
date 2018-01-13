from datetime import datetime
from mongoengine import Document, StringField, IntField, ListField, DateTimeField

class Animal(Document):
    name = StringField(required=True)
    age = IntField()
    breed = ListField()
    arrived_date = DateTimeField(default=datetime.now())
    description = StringField()

    def __init__(self, name, age, breed, arrived_date, description, *args, **kwargs):
        super(Document, self).__init__(*args,**kwargs)
        self.name = name
        self.age = age
        self.breed = breed
        self.arrived_date = datetime.strptime(arrived_date, '%Y-%m-%d')
        self.description = description
