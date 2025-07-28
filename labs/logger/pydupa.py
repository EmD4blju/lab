import logging
import logging.config
import yaml
from queue import Queue
from logging.handlers import QueueHandler, QueueListener
import os
from typing import override


class SessionFileRouter(logging.Handler):
    def __init__(self, base_dir="logs"):
        super().__init__()
        self.base_dir = base_dir
        self.handlers = {}
        os.makedirs(self.base_dir, exist_ok=True)

    @override
    def emit(self, record: logging.LogRecord):
        session_id = getattr(record, "session_id", "unknown")
        handler = self.get_handler_for_session(session_id)
        handler.emit(record)

    def get_handler_for_session(self, session_id):
        if session_id not in self.handlers:
            file_path = os.path.join(self.base_dir, f"session_{session_id}.log")
            handler = logging.FileHandler(file_path)
            handler.setLevel(logging.INFO)
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            self.handlers[session_id] = handler
        return self.handlers[session_id]
    

with open('labs/logger/config.yaml', 'r') as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)
    

log_queue = Queue()

queue_handler = QueueHandler(log_queue)
session_router_handler = SessionFileRouter()

logger = logging.getLogger("my_app_logger")
logger.addHandler(queue_handler)

print(logger)



listener = QueueListener(log_queue, session_router_handler, respect_handler_level=True)
listener.start()

# Użyj własnego loggera
#logger = logging.getLogger('my_app_logger')

# Przykładowe logi
logger.debug("To jest DEBUG", extra={"session_id": "abc123"})
logger.info("To jest INFO", extra={"session_id": "abc123"})
logger.warning("To jest WARNING", extra={"session_id": "abc321"})
logger.error("To jest asdfasdfERROR", extra={"session_id": "abc321"})
logger.critical("To jest CRITICAL", extra={"session_id": "abc123"})

listener.stop()

