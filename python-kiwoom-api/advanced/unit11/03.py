import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)

file_handler = logging.FileHandler("mylog2.txt")
logger.addHandler(file_handler)

logger.info("this is info")