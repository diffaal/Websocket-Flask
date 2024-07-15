from flask import Response
from http import HTTPStatus
from marshmallow import ValidationError

from websocket_api.enums.response_message import ResponseMessage
from websocket_api.tools.app_logger import error_logger
from websocket_api.tools.response import make_json_response

def validation_error_handler(e: ValidationError) -> Response:
    return make_json_response(HTTPStatus.UNPROCESSABLE_ENTITY, e.messages, None)

def exception_handler(e: Exception) -> Response:
    error_logger(e, True)
    return make_json_response(HTTPStatus.INTERNAL_SERVER_ERROR, ResponseMessage.INTERNAL_SERVER_ERROR.value, None)
