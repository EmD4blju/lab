import logging
import logging.handlers
import queue
import threading
import time

def worker(logger, thread_id):
    for i in range(5):
        logger.info(f'Thread {thread_id} log entry {i}')
        time.sleep(0.2)
        

def main():
    log_queue = queue.Queue(-1)
    
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(
        logging.Formatter("[%(threadName)s] %(msg)s")
    )
    
    file_handler = logging.FileHandler("async_log.txt", mode='w')
    file_handler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(threadName)s %(message)s"))
    
    listener = logging.handlers.QueueListener(log_queue, console_handler, file_handler)
    listener.start()
    
    logger = logging.getLogger('asyncLogger')
    logger.setLevel(logging.DEBUG)
    queue_handler = logging.handlers.QueueHandler(log_queue)
    logger.addHandler(queue_handler)
    
    threads = []
    for i in range(3):
        t = threading.Thread(target=worker, args=(logger, i), name=f'Worker-{i}')
        t.start()
        threads.append(t)
    
    for t in threads:
        t.join()
    
    listener.stop()
    
if __name__ == '__main__':
    main()