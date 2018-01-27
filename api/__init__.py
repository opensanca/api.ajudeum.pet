"""
Módulo inicializador da aplicação de API
"""
from flask import Flask
from mongoengine import connect
from api.animals.endpoints import ANIMAL
import settings


connect(host=settings.MONGODB_URI)


def create_app():
    """Cria o app"""
    app = Flask(__name__)
    app.register_blueprint(ANIMAL)
    return app
