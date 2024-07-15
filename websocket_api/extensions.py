import socketio
from flask import Flask
from flask_marshmallow  import Marshmallow
from logging import Logger

from websocket_api.config import CONFIG

logger = Logger("WEBSOCKET API FLASK")
ma = Marshmallow()
sio_client  = socketio.Client()

def register_extensions(app: Flask):
    logger.addHandler(app.logger)
    ma.init_app(app)
    sio_client.connect(CONFIG.WEBSOCKET_SERVER_URL, transports=["websocket"], namespaces=["/private"])
