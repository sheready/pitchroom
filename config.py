import os
class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql+psycopg2://moringa:Access@localhost/pitch'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    SECRET_KEY = '\xbc&\x9c\x1d#9\xc9\xb8Fh\x17\x00u\xefX\xbb\x12\xd4i\xb3\xb2\xfd\xdf\xe8'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or 'postgresql+psycopg2://moringa:Access@localhost/pitch'


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    DATABASE_URL = 'postgresql+psycopg2://moringa:Access@localhost/pitch'
    DEBUG = True 

config_options = {
'development':DevConfig,
'production':ProdConfig
}

