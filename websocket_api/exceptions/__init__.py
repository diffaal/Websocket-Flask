from flask import Flask
from marshmallow import ValidationError

from websocket_api.exceptions.error_handler import (
    exception_handler,
    validation_error_handler
)

def register_error_handler(app: Flask):
    app.register_error_handler(Exception, exception_handler)
    app.register_error_handler(ValidationError, validation_error_handler)
