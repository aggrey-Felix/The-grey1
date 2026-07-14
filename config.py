import os
from datetime import timedelta


def _get_default_db_path():
    sqlite_path = os.environ.get('DB_PATH')
    if sqlite_path:
        return sqlite_path

    instance_path = os.path.join(os.path.dirname(__file__), 'instance')
    try:
        os.makedirs(instance_path, exist_ok=True)
        return os.path.join(instance_path, 'blog.db')
    except OSError:
        return os.path.join('/tmp', 'blog.db')


class Config:
    """Base configuration"""
    db_path = _get_default_db_path()
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', f'sqlite:///{db_path.replace(chr(92), "/")}')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')
    PERMANENT_SESSION_LIFETIME = timedelta(days=7)

class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    TESTING = False

class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    TESTING = False

class TestingConfig(Config):
    """Testing configuration"""
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
