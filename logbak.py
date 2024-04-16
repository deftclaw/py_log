import logging
import sys
from etc.config import LOGLEVEL

log = logging.getLogger(__name__)
logging.basicConfig(
    datefmt='%Y-%m-%d %H:%M:%S',
    filemode='a',
    filename='/tmp/test4.log',
    format='{asctime} {levelname} {filename}:{lineno}: {message}',
    style='{',
)
logcfg = {

    }

print(f"Loglevel read as: {LOGLEVEL}")

match LOGLEVEL:
    case "DEBUG":
        log.setLevel(logging.DEBUG)
        print("Debug logging-level selected")

    case "INFO":
        log.setLevel(logging.INFO)
        print("Info logging-level selected")

    case "WARNING":
        log.setLevel(logging.WARNING)
        print("Warning logging-level selected")

    case _:
        print("LOGLEVEL in etc/config.py should be one of [DEBUG, INFO, WARNING]")
        raise Exception
