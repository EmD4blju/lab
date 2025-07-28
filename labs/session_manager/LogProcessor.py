import logging
import logging.config
from typing import override
import os
from queue import Queue
from logging.handlers import QueueHandler, QueueListener
import yaml
import time
import atexit

class SessionFileRouter(logging.Handler):
    def __init__(self, base_dir="logs2"):
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

    def cleanup_handler(self, session_id):
        handler = self.handlers.pop(session_id, None)
        if handler:
            handler.close()
            try:
                os.remove(os.path.join(self.base_dir, f"session_{session_id}.log"))
            except FileNotFoundError:
                pass

class LogProcessor():
    def __init__(self):  
        
        
        with open('labs/session_manager/config.yaml','r') as config_file:
            logging_config = yaml.load(config_file, Loader=yaml.FullLoader)
            
        logging.config.dictConfig(config=logging_config) 
         
        self.session_router = SessionFileRouter()
        self.queue = Queue()
        self.queue_handler = QueueHandler(self.queue)      
        
        self.user_logger = logging.getLogger('user_logger')
        print(self.user_logger)
        self.user_logger.addHandler(self.queue_handler)      
        
        self.queue_listener = QueueListener(self.queue, self.session_router, respect_handler_level=True)
        self.queue_listener.start()
        atexit.register(self.shutdown)
        
    def clean_logger(self, session_id):
        self.session_router.cleanup_handler(session_id)
        
    def shutdown(self):
        self.queue_listener.stop()
        
    
        