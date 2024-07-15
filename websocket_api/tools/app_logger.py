from traceback import format_exc

from websocket_api.extensions import logger

def error_logger(e, traceback = False):
    logger.error(f"Exception Type::{type(e).__name__}")
    logger.error(f"Syserr::{e}")
    if traceback:
        logger.error(f"Traceback::{format_exc()}")