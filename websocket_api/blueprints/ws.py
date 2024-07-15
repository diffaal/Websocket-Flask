from flask import Blueprint
from flask_restful import Api

from websocket_api.resources.private import WebsocketPrivateMessageResource

ws_bp = Blueprint("ws_bp", __name__, url_prefix="/api/v1/ws")
ws_api = Api(ws_bp)
ws_api.add_resource(WebsocketPrivateMessageResource, "/private-message")