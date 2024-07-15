from flask_socketio import emit
from flask_socketio.namespace import Namespace

from websocket_server.extensions import redis_client

class UserStatus(Namespace):
    def on_online(self, data):
        print("online")
        user_id = data["user_id"]
        redis_client.set(f"user_status:{user_id}", "online")
        emit("online", data, broadcast=True)

    def on_offline(self, data):
        print("offline")
        user_id = data["user_id"]
        redis_client.set(f"user_status:{user_id}", "offline")
        emit("offline", data, broadcast=True)
