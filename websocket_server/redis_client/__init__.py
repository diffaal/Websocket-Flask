from redis import Redis, ConnectionPool

from websocket_server.config import CONFIG

def register_redis_client(redis_client: Redis):
    redis_pool = ConnectionPool()
    redis_client.__init__(
        host=CONFIG.REDIS_HOST,
        port=CONFIG.REDIS_PORT,
        db=CONFIG.REDIS_DB,
        connection_pool=redis_pool
    )
    