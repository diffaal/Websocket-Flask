from flask_socketio import SocketIO

from websocket_server.handlers.general import GeneralMessage
from websocket_server.handlers.private import PrivateMessage
from websocket_server.handlers.user_status import UserStatus

def register_socket_namespace(socketio: SocketIO):
    socketio.on_namespace(GeneralMessage("/"))
    socketio.on_namespace(PrivateMessage("/private"))
    socketio.on_namespace(UserStatus("/user-status"))
