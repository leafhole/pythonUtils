# -*- coding: utf8 -*-

import time
import logging
import os


def init_logger(name, logfile_name=None):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(name)s - %(message)s")
    ch = None
    if logfile_name is None:
        ch = logging.StreamHandler()
    else:
        logDir = os.path.dirname(logfile_name)
        if not os.path.exists(logDir):
            os.makedirs(logDir)
            pass
        now = time.localtime()
        suffix = '.%d%02d%02d' % (now.tm_year, now.tm_mon, now.tm_mday)
        ch = logging.FileHandler(logfile_name+suffix)
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger

def Main():
    logger = init_logger("test","logTest")
    logger.debug("it a log")
    pass


if __name__ == "__main__":
    Main()
