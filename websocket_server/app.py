from websocket_server import create_app
from websocket_server.extensions import redis_client

app, sio_server = create_app()

if __name__ == "__main__":
    sio_server.run(app)
    redis_client.close()
