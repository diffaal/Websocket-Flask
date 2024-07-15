import redis
from flask import Flask

from logging import Logger

from websocket_server.redis_client import register_redis_client

logger = Logger("WEBSOCKET SERVER FLASK")
redis_client = redis.Redis()

def register_extensions(app: Flask):
    logger.addHandler(app.logger)
    register_redis_client(redis_client)
