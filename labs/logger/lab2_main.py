import logging
import debug.helper as helper

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(levelname)s] %(name)s %(message)s'
)

logger = logging.getLogger(__name__)

logger.info('Hello from main.py')
helper.say_hello()
helper.say_something_weird()

