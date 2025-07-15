import logging

logger = logging.getLogger(__name__)

def say_hello():
    logger.info("Hello from the helper module!")

def say_something_weird():
    logger.debug("Debug-level weird helper fact.")
