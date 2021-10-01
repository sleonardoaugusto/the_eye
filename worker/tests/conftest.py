import os
from pathlib import Path

import pytest
from faker import Faker

from settings import Environment


@pytest.fixture
def faker() -> Faker:
    return Faker()


@pytest.fixture(autouse=True, scope='session')
def setup():
    os.environ['ENVIRONMENT'] = Environment.TEST.value


@pytest.fixture(autouse=True)
def delete_database():
    yield
    db_file = 'eye_test.db'
    Path(Path().parent).joinpath(db_file).unlink()
