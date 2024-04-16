import logging
import sys
from etc.config import LOGLEVEL

def configure_logger(name):
    cfg = {
        'fmt': logging.Formatter(
            datefmt='%Y-%m-%d %H:%M:%S',
            fmt='{asctime} {levelname} {filename}:{lineno}: {message}',
            style='{',
        )
    }
