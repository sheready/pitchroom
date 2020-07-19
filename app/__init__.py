from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options, Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_simplemde import SimpleMDE
from sqlalchemy import create_engine

bootstrap = Bootstrap()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
simple = SimpleMDE()

def create_app(config_name):
    app = Flask(__name__)


    # Creating the app configurations
    app.config.from_object(config_options[config_name])
    app.config.from_object(Config)
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')

    DB_URI = app.config['SQLALCHEMY_DATABASE_URI']
    engine = create_engine(DB_URI)
    
    # Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    simple.init_app(app)
    login_manager.init_app(app)


    return app