from flask_migrate import Migrate
from .db import db

migrate = Migrate()

def configure(app):
    migrate.init_app(app, db)