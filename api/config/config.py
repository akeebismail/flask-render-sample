import os
from decouple import config
from datetime import timedelta


BASE_DIR = os.path.dirname(os.path.realpath(__file__))

class Config:
    SECRET_KEY=config('SECRET_KEY','Secret')
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes = 30)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(minutes = 30)
    JWT_SECRET_KEY=config('JWT_SECRET_KEY')
    
    
class DevConfig(Config):
    DEBUG=True
    SQLALCHEMY_ECHO =True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' +os.path.join(BASE_DIR, 'db2.sqlite3')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
class TestConfig(Config):
    
    pass

class ProdConfig(Config):
    pass
    
    
config_dict={
    'dev': DevConfig,
    'prod': ProdConfig,
    'test': TestConfig
}