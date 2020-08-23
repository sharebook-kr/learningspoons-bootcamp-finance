import logging
import logging.handlers
import time

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s')

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

file_handler = logging.handlers.TimedRotatingFileHandler(filename="log",
                                                         when = "M", 
                                                         interval=1)
file_handler.setFormatter(formatter)

# add handler to logger
logger.addHandler(stream_handler)
logger.addHandler(file_handler)

while True:
    logger.info("this is info")
    time.sleep(10)