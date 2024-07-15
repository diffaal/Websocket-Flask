from flask import (
    request,
    Response
)
from flask_restful import Resource
from http import HTTPStatus

from websocket_api.extensions import sio_client
from websocket_api.enums.response_message import ResponseMessage
from websocket_api.schemas.private_message import private_message_schema
from websocket_api.tools.response import make_json_response

class WebsocketPrivateMessageResource(Resource):
    def get(self):
        return "Hello World"
    
    def post(self) -> Response:
        request_data = private_message_schema.load(request.json)
        sio_client.call("message", request_data, namespace="/private")
        return make_json_response(HTTPStatus.OK, ResponseMessage.SUCCESS.value, None)
