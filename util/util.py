import logging

from settings import LOG_LEVEL


def is_one_word(string: str):
    for c in string:
        if c.isspace():
            return False
    return True

def char_count(string: str):
    return len(string)

def strip_whitespace(string: str):
    return string.strip

def get_logger(logger_name, log_level=logging.INFO):
    logger = logging.getLogger(logger_name)
    logger.setLevel(log_level)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(LOG_LEVEL)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    return logger
