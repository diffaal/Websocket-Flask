from flask import Flask
from flask_socketio import SocketIO

from websocket_server.config import Config, CONFIG
from websocket_server.extensions import register_extensions
from websocket_server.handlers import register_socket_namespace

def create_app():
    app = Flask("WEBSOCKET SERVER FLASK")
    app.config.from_object(Config)
    register_extensions(app)

    sio_server = SocketIO(app, message_queue=CONFIG.REDIS_STRING_CONNECTION)
    register_socket_namespace(sio_server)

    return app, sio_server
