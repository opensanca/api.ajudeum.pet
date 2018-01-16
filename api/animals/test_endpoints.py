from .endpoints import animals


def test_animals():
    assert animals() == '"Hello animals world!"'
