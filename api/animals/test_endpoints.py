"""
Módulo de teste para endpoints.py
"""

from datetime import datetime
from json import loads
from .model import Animal
from .endpoints import animals


def test_animals():
    """Testa o fluxo básico do endpoint de animais"""
    animal = Animal(name='Dog 1',
                    age=64,
                    breed=['lontras'],
                    arrived_date=datetime(2018, 1, 1),
                    description="um cachorro do barulho")
    animal.save()
    response = loads(animals())
    assert len(response) == 1
    assert response[0]['id'] == str(animal.id)
