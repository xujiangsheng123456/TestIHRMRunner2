import logging
import logging.handlers
import os
HEADERS = {"Content-Type": "application/json"}
EMP_ID = ""

base_path = os.path.dirname(os.path.abspath(__file__))
def init_logging():
    logger = logging.getLogger()
    logger.setLevel(level=logging.INFO)
    sh = logging.StreamHandler()

    fh = logging.handlers.TimedRotatingFileHandler(base_path + "./log/ihrm123.log", when="M",interval=1,backupCount=3)
    fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    format = logging.Formatter(fmt)
    sh.setFormatter(format)
    fh.setFormatter(format)
    logger.addHandler(sh)
    logger.addHandler(fh)