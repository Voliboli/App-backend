from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_cors import CORS
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

def create_app():
    """Create Flask application."""
    app = Flask(__name__)
    cors = CORS(app)
    app.config.from_object('config.DevConfig')

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    with app.app_context():
        # Import blueprints 
        from .api import players_api_blueprint

        # Register Blueprints
        app.register_blueprint(players_api_blueprint)

        # Create database
        db.create_all()

        return app
