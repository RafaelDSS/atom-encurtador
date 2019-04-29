from flask import Flask
from config import config

# Factory app


def create_app():
    app = Flask(__name__)

    app.config.from_object(config['production'])

    # Extensions
    from app import ext
    ext.configure(app)

    # Blueprints
    from app import blueprints
    blueprints.configure(app)

    return app
