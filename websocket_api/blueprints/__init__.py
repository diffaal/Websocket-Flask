from flask import Flask

from websocket_api.blueprints.ws import ws_bp

def register_blueprints(app: Flask):
    app.register_blueprint(ws_bp)
