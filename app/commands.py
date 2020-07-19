import click
from flask.cli import with_appcontext

from . import db
from .models import User,Votes,Comments,Pitch,PitchCategory

@click.command(name='create_tables')
@with_appcontext
def create_tables():
    db.create_all()