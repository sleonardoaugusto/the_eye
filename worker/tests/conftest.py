import os

os.environ['ENVIRONMENT'] = 'test'

from pathlib import Path

import pytest
from faker import Faker

from db import SessionLocal, Base, engine


@pytest.fixture
def faker() -> Faker:
    return Faker()


@pytest.fixture(autouse=True)
def db():
    Base.metadata.create_all(engine)
    db = SessionLocal()
    return db


@pytest.fixture(autouse=True)
def delete_database():
    yield
    db_file = 'eye_test.db'
    Path(Path().parent).joinpath(db_file).unlink()
