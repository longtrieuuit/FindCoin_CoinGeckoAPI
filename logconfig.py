import os.path
import glob, os
from datetime import datetime
import logging
import sys
import time
import logging, logging.handlers


def setup_custom_logger_rtsp(name):
    formatter = \
        logging.Formatter(fmt='%(asctime)s %(levelname)-2s %(message)s'
                          , datefmt='%Y-%m-%d %H:%M:%S')
    handler = logging.handlers.RotatingFileHandler("app_"+name+".log", maxBytes=10000000, backupCount=2)
    handler.setFormatter(formatter)
    screen_handler = logging.StreamHandler()
    screen_handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    logger.addHandler(screen_handler)
    return logger

logger_en = setup_custom_logger_rtsp('en')
logger_coin = setup_custom_logger_rtsp('coingeco')
