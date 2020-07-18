from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask import Flask
from .config import DevConfig
from .config import config_options



db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__,instance_relative_config = True)

    app.config.from_object(DevConfig)
    app.config.from_pyfile("config.py")

    # Initializing flask extensions
    bootstrap = Bootstrap(app)
    bootstrap.init_app(app)
    db.init_app(app)

from app import views
from app import error