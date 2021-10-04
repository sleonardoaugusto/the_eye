import enum
import os

from dotenv import load_dotenv

load_dotenv('.env')


class Environment(enum.Enum):
    DEVELOPMENT = 'development'
    TEST = 'test'


class BaseSettings:
    broker_url = os.environ.get('CELERY_BROKER_URL')
    result_backend = os.environ.get('CELERY_RESULT_BACKEND')


class TestSettings(BaseSettings):
    db_url = os.environ.get('DATABASE_TEST_URL')


class DevSettings(BaseSettings):
    db_url = os.environ.get('SQLALCHEMY_DATABASE_URL')


class Settings:
    @property
    def environment(self):
        if os.environ.get('ENVIRONMENT') == Environment.TEST.value:
            return Environment.TEST
        else:
            return Environment.DEVELOPMENT

    def get_settings(self):
        settings = (
            TestSettings() if self.environment == Environment.TEST else DevSettings()
        )
        return settings


settings = Settings().get_settings()
