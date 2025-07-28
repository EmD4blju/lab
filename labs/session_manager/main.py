import LogProcessor as lp
import ServiceProcessor as sp
import SessionManager as sm
from uuid import uuid4
from time import sleep


if __name__ == '__main__':
    log_proc = lp.LogProcessor()
    ses_man = sm.SessionManager(log_proc)
    serv_proc = sp.ServiceProcessor(ses_man)
    logger = ses_man.log_processor.user_logger
    
    
    for i in range(5):
        uuid = f'{i} str(uuid4())'
        ses_man.create_session(uuid)
        logger.warning("Hello from user!", extra={"session_id": uuid})
    

    
    while True:
        print(log_proc.session_router.handlers)
        sleep(2)