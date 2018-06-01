import os


class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    _BASE_DIR = os.path.dirname(__file__)
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', f'sqlite:///{os.path.join(_BASE_DIR, "ajude.um.pet.db")}')
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
    SERVER_NAME = 'localhost:5000'
