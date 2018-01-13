from flask import Blueprint, request, abort
import json

animal = Blueprint("animal", __name__, url_prefix="/animals")

@animal.route("/", methods = ["GET"])
def animals(): return "Hello animals world!"

@animal.route("/", methods = ["POST"])
def create_animal():
    if not request.json:
        abort(400)

    return json.dumps({})