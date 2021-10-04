import os

os.environ['ENVIRONMENT'] = 'test'

from pathlib import Path

import pytest
from faker import Faker

from db import SessionLocal


@pytest.fixture
def faker() -> Faker:
    return Faker()


@pytest.fixture(autouse=True)
def delete_database():
    yield
    db_file = 'eye_test.db'
    Path(Path().parent).joinpath(db_file).unlink()


@pytest.fixture
def db():
    db = SessionLocal()
    return db
