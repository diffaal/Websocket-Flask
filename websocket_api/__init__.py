from flask import Flask

from websocket_api.config import Config
from websocket_api.extensions import register_extensions
from websocket_api.blueprints import register_blueprints
from websocket_api.exceptions import register_error_handler

def create_app():
    app = Flask("WEBSOCKET API FLASK")
    app.config.from_object(Config)
    register_extensions(app)
    register_blueprints(app)
    register_error_handler(app)

    return app