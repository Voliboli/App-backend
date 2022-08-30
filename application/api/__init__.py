from flask import Blueprint

players_api_blueprint = Blueprint('players_api_blueprint', __name__)

from . import routes
