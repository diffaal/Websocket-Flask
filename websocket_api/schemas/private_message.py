from marshmallow import fields

from websocket_api.extensions import ma

class PrivateMessageSchema(ma.Schema):
    room = fields.String(
        required=True, 
        error_messages=dict(
            required="room is required"
        )
    )
    data = fields.Dict(keys=fields.String(), values=fields.Raw())

private_message_schema = PrivateMessageSchema()
