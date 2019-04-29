from . import db, migrate


def configure(app):
    db.configure(app)
    migrate.configure(app)
