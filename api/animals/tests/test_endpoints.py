from datetime import datetime, date
from http import HTTPStatus

from flask import url_for

from api.animals.model import Animal


def test_get_all_animals(client, session):
    response = client.get(url_for('animal.animals'))

    assert not response.json

    animal = Animal(name='Dog 1',
                    age=64,
                    breed='lontras',
                    arrived_date=datetime(2018, 1, 1),
                    description="um cachorro do barulho")

    session.add(animal)
    session.commit()

    response = client.get(url_for('animal.animals'))

    assert response.status_code == HTTPStatus.OK
    assert len(response.json) == 1
    assert response.json[0]['id'] == animal.id


def test_create_animal(client, session):
    assert Animal.query.count() == 0

    data = {
        'name': 'Doguito',
        'age': '2',
        'breed': 'SRD',
        'description': 'Doguito preto e branco',
        'arrived_date': '2018-01-21',
    }

    response = client.post(url_for('animal.create_animal'), json=data)

    assert response.status_code == HTTPStatus.OK
    assert Animal.query.count() == 1

def test_update_animal(client, session):
    animal = Animal(name='Dog 2',
                    age=5,
                    breed='vira-lata',
                    arrived_date=date(2018, 1, 10),
                    description="um unicornio do barulho")

    animal.save()

    mock_data = {
        'id': animal.id,
        'name': 'Dog 2 editado',
        'age': 6,
        'breed': 'vira-lata',
        'description': 'unicornio preto e branco',
        'arrived_date': '2018-01-10',
    }

    params = {'animal_id': animal.id}
    response = client.put(url_for('animal.update_animal', **params), json=mock_data)

    assert response.status_code == HTTPStatus.OK
    assert response.get_json().items() == mock_data.items()

    animal = Animal.query.filter_by(id=animal.id).one()

    assert animal.name == mock_data['name']
    assert animal.age == mock_data['age']
    assert animal.description == mock_data['description']


def test_delete_animal(client, session):
    animal = Animal(name='Dog 2',
                    age=5,
                    breed='cachorro',
                    arrived_date=datetime(2018, 1, 10),
                    description="um unicornio do barulho")

    animal.save()
    params = {'animal_id': animal.id}
    response = client.delete(url_for('animal.delete_animal', **params))

    assert response.status_code == HTTPStatus.OK
    assert not Animal.query.filter_by(id=animal.id).count()
