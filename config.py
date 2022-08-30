from os import environ, path
from dotenv import load_dotenv
from sqlalchemy.engine.url import URL

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

class Config:
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'

class ProdConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False

class DevConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = URL(
            drivername='postgresql',
            username=environ['PGUSER'],
            password=environ['PGPASSWORD'],
            host=environ['DATABASE_IP'],
            port=environ['DATABASE_PORT']
    )
    PORT = environ['PORT']
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LOGIN_PAGE = "login"
    SECRET_KEY = "secret"
    ADMIN_USER = "tp7220"
    GOOGLE_CLIENT_ID = ""
    FB_CLIENT_ID = ""
    FB_CLIENT_SECRET = ""
