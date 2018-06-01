import uuid
from datetime import datetime

from api import db


class Animal(db.Model):

    __tablename__ = 'animal'

    id = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    breed = db.Column(db.String(30), nullable=False)
    arrived_date = db.Column(db.Date, default=datetime.utcnow)
    description = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'<Animal: {self.name}>'

    def __json__(self):
        return ['id', 'name', 'age', 'breed', 'arrived_date', 'description']

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        for field in data:
            setattr(self, field, data[field])

        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
