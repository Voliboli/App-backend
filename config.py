from os import environ, path
from dotenv import load_dotenv
from sqlalchemy.engine.url import URL

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

class ProdConfig:
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False

class DevConfig:
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = URL(
            drivername='postgresql',
            username=environ['POSTGRES_USERNAME'],
            password=environ['USER_PASSWORD'],
            host=environ['DATABASE_IP'],
            port=5432,
            database=environ['POSTGRES_DATABASE'],
            query={}
    )
    PORT = environ['PORT']
    SQLALCHEMY_TRACK_MODIFICATIONS = False