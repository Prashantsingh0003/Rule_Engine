

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config.settings import SQLALCHEMY_DATABASE_URI

# Initialize SQLAlchemy
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # Set up the database connection URI from settings.py
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize the database with Flask app
    db.init_app(app)

    # Register API routes
    from app.api import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    # Create all tables in the database if they do not exist
    with app.app_context():
        db.create_all()

    return app
