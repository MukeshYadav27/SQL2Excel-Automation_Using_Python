# logger.py

import os
from datetime import datetime

from config import LOG_FOLDER

os.makedirs(LOG_FOLDER, exist_ok=True)

LOG_FILE = os.path.join(LOG_FOLDER, "automation.log")


def write_log(message):
    """
    Write messages to automation.log
    """

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_FILE, "a", encoding="utf-8") as file:

        file.write(f"[{current_time}] {message}\n")


def log_error(error):
    """
    Write error messages.
    """

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_FILE, "a", encoding="utf-8") as file:

        file.write(f"[{current_time}] ERROR : {error}\n")