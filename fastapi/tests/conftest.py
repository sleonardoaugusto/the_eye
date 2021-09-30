import pytest
from faker import Faker
from starlette.testclient import TestClient

from main import app


@pytest.fixture
def client():
    return TestClient(app=app)


@pytest.fixture
def faker():
    return Faker()
