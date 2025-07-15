import logging

logger = logging.getLogger('app')
logger.setLevel(level=logging.DEBUG)


console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_format = logging.Formatter("[%(levelname)s] %(name)s: %(message)s")
console_handler.setFormatter(console_format)

file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.DEBUG)
file_format = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
file_handler.setFormatter(file_format)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

logger.debug("Debug message (should only be in file)")
logger.info("Info message")
logger.warning("Warning message")
logger.error("Error occurred")