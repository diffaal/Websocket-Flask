import os
from logging.config import dictConfig
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = "secret!"
    PROPAGATE_EXCEPTIONS = True

    WEBSOCKET_SERVER_URL = os.getenv("WEBSOCKET_SERVER_URL")

    LOGGING_CONFIG = {
        'version': 1,
        'formatters': {
            'standard': {
                'format': '%(asctime)s | %(name)s | %(levelname)s | %(message)s',
            },
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'standard',
                'level': 'DEBUG',
            },
            'file': {
                'class': 'logging.FileHandler',
                'filename': 'app.log',
                'formatter': 'standard',
                'level': 'DEBUG',
            },
        },
        'loggers': {
            '': {  # root logger
                'handlers': ['console', 'file'],
                'level': 'DEBUG',
                'propagate': True,
            },
        }
    }

    dictConfig(LOGGING_CONFIG)

CONFIG = Config()
