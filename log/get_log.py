import logging


def get_logger() -> logging:
    format = '%(levelname)s:%(funcName)s:%(message)s'
    logging.basicConfig(format=format, level=logging.DEBUG)
    return logging
