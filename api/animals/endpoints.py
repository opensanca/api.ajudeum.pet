from datetime import datetime
from flask import Blueprint, request, abort
from ..common.utils import json_result
from .model import Animal

animal = Blueprint("animal", __name__, url_prefix="/animals")

@animal.route("/", methods = ["GET"])
@json_result
def animals():
    return list(map(lambda x: {
        'name': x.name,
        'age': x.age,
        'breed': x.breed,
        'description': x.description,
        'arrived_date': x.arrived_date.date().isoformat(),
        'id' : str(x.id)
    }, Animal.objects))


@animal.route("/", methods = ["POST"])
@json_result
def create_animal():
    if not request.json:
        abort(400)
    data = request.json
    
    name = data['name']
    age = data['age']
    breed =  data['breed']
    description = data['description']
    arrived_date = datetime.strptime(data['arrived_date'], '%Y-%m-%d')
    animal_doc = Animal(name=name, age=age, breed=breed, description=description, arrived_date=arrived_date)

    animal_doc.save()
    return str(animal_doc.id)

@animal.route("/<animal_id>", methods = ["PUT"])
@json_result
def update_animal(animal_id):
    return 'test'

@animal.route("/<animal_id>", methods = ["DELETE"])
@json_result
def delete_animal(animal_id):
    return {}
