import socketio

def send_private_message(data):
    sio = socketio.Client()
    sio.connect('http://localhost:5000', transports=["websocket"], namespaces=["/private"])
    resp = sio.call("message", data, namespace="/private")
    sio.disconnect()

async def async_send_private_message(data):
    sio = socketio.AsyncClient()
    await sio.connect('http://localhost:5000', transports=["websocket"], namespaces=["/private"])
    resp = await sio.call("message", data, namespace="/private")
    await sio.disconnect()
