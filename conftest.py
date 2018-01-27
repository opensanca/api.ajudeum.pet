"""Módulo de configuração do pytest"""

import pytest
from api import create_app


@pytest.fixture
def app():
    """Fábrica de contexto Flask."""
    return create_app()
