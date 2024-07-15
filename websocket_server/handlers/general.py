from flask_socketio import emit
from flask_socketio.namespace import Namespace


class GeneralMessage(Namespace):
    def on_connect(self):
        print("connect")
        emit("message", "Client connected", broadcast=True)

    def on_disconnect(self):
        print("disconnect")
        emit("message", "Client disconnected", broadcast=True)

    def on_message(self, data):
        print(data)
        emit('message', data, broadcast=True)
