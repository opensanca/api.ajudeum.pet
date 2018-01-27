"""
Módulo de API para gerenciamento de animais
"""
from flask import Blueprint, request
from ..common.utils import json_result
from ..common.exceptions import InvalidInput
from .model import Animal
from .schemas import AnimalSchema


ANIMAL = Blueprint("animal", __name__, url_prefix="/animals")


@ANIMAL.route("/", methods=["GET"])
@json_result
def animals():
    """ Retorna uma lista de animais """
    return list(map(lambda x: {
        'name': x.name,
        'age': x.age,
        'breed': x.breed,
        'description': x.description,
        'arrived_date': x.arrived_date.date().isoformat(),
        'id': str(x.id)
    }, Animal.objects))


@ANIMAL.route("/", methods=["POST"])
@json_result
def create_animal():
    """Endpoint que cadastra dados do animal"""
    schema = AnimalSchema()
    data, errors = schema.load(request.json)
    if errors:
        raise InvalidInput(errors)

    animal_doc = Animal(**data)
    animal_doc.save()
    return str(animal_doc.id)


@ANIMAL.route("/<animal_id>", methods=["PUT"])
@json_result
def update_animal(animal_id):
    """Atualiza dados de um animal já cadastrado"""
    schema = AnimalSchema()
    data, errors = schema.load(request.json)
    if errors:
        raise InvalidInput(errors)

    animal_update_doc = Animal.objects.get(id=animal_id)
    animal_update_doc.name = data['name']
    animal_update_doc.age = data['age']
    animal_update_doc.breed = data['breed']
    animal_update_doc.description = data['description']
    animal_update_doc.arrived_date = data['arrived_date']
    animal_update_doc.save()
    return str(animal_update_doc.id)


@ANIMAL.route("/<animal_id>", methods=["DELETE"])
@json_result
def delete_animal(animal_id):
    """Remove um animal cadastrado no banco de dados"""
    animal = Animal.objects.get(id=animal_id)
    animal.delete()
