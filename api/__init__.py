from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from api.common.exceptions import InvalidInput
from api.common.encoder import AlchemyJSONEncoder


db = SQLAlchemy()
migrate = Migrate()


def handle_invalid_input(error):
    """Trata exceções do tipo InvalidInput,
    retornando o dicionário de mensagens e
    o status 400 BAD REQUEST"""
    response = jsonify(error.errors)
    response.status_code = error.status_code
    return response


def create_app(environment='Development'):
    app = Flask(__name__)
    app.config.from_object(f'api.config.{environment}Config')
    app.json_encoder = AlchemyJSONEncoder

    CORS(app)

    db.init_app(app)
    migrate.init_app(app, db)

    from api.animals.endpoints import ANIMAL
    app.register_blueprint(ANIMAL)
    app.register_error_handler(InvalidInput, handle_invalid_input)

    return app
