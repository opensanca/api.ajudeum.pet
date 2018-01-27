import pytest
from api import create_app


@pytest.fixture
def app():
    return create_app()
