from flask_socketio import emit, join_room, leave_room
from flask_socketio.namespace import Namespace


class PrivateMessage(Namespace):
    def on_connect(self):
        print("connect private")
        emit("message", "Client connected", broadcast=True)

    def on_disconnect(self):
        print("disconnect private")
        emit("message", "Client disconnected", broadcast=True)

    def on_join(self, data):
        print(data)
        room = data['room']
        join_room(room)
        emit('message', f'User has joined room: {room}', to=room)
    
    def on_leave(self, data):
        room = data['room']
        leave_room(room)
        emit('message', f'User has left room: {room}', to=room)

    def on_message(self, data):
        print(data)
        room = data["room"]
        message = data["data"]
        emit('message', message, to=room)
