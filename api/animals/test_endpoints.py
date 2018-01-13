from datetime import datetime
from json import loads
from .model import Animal
from .endpoints import animals


def test_animals():
    d1 = Animal(name='Dog 1', age=64, breed = ['lontras'], arrived_date = datetime(2018,1,1), description ="um cachorro do barulho")
    d1.save()
    rs = loads(animals())
    assert len(rs)==1
    assert rs[0]['id']== str(d1.id)

