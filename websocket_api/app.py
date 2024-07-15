from websocket_api import create_app
from websocket_api.extensions import sio_client

app = create_app()

if __name__ == "__main__":
    app.run()
    sio_client.disconnect()
