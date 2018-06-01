from flask import Blueprint, request, jsonify

from api.animals.model import Animal
from api.animals.schemas import AnimalSchema
from api.common.exceptions import InvalidInput


ANIMAL = Blueprint("animal", __name__, url_prefix="/animals")


@ANIMAL.route("/", methods=["GET"])
def animals():
    return jsonify(Animal.query.all())


@ANIMAL.route("/", methods=["POST"])
def create_animal():
    schema = AnimalSchema()
    data, errors = schema.load(request.get_json())

    if errors:
        raise InvalidInput(errors)

    animal = Animal(**data)
    animal.save()

    return jsonify(animal)


@ANIMAL.route("/<animal_id>", methods=["PUT"])
def update_animal(animal_id):
    schema = AnimalSchema()
    data, errors = schema.load(request.get_json())

    if errors:
        raise InvalidInput(errors)

    animal = Animal.query.filter_by(id=animal_id).one()
    animal.update(data)

    return jsonify(animal)


@ANIMAL.route("/<animal_id>", methods=["DELETE"])
def delete_animal(animal_id):
    animal = Animal.query.filter_by(id=animal_id).one()
    animal.delete()

    return ''
