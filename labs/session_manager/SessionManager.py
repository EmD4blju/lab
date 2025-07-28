from time import time, sleep
from LogProcessor import LogProcessor
from threading import Thread

class SessionManager():
    """SessionManager is used for managing session-specific informations. It is responsible for deleting any information
    """
    
    def __init__(self, log_processor: LogProcessor):
        self.session_store = dict()
        self.log_processor = log_processor
        Thread(target=self._cleanup_session_storage, daemon=True).start()
    
    def create_session(self, session_id):
        self.session_store[session_id] = {
            'history': f'InMemoryChatMessageHistory({session_id})',
            'timestamp': time()
        }
    
    def _cleanup_session_storage(self, ttl_seconds=5):
        """This is daemon function used to clear session storage from memory. Any chat history that session_id has expired is removed from session storage.

        Args:
            ttl_seconds (int, optional): Expiration time. Defaults to 20 seconds.
        """
        print("daemon started")
        while True:
            now = time()
            expired_keys = [
                key for key, val in self.session_store.items()
                if now - val['timestamp'] > ttl_seconds
            ]
            for key in expired_keys:
                print(f"Deleting expired key: {key}")
                del self.session_store[key]
                self.log_processor.clean_logger(key)
            sleep(5)