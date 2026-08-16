import os
import logging
from logging.handlers import TimedRotatingFileHandler

# 1. Path to this file: .../MLOPS-PYTORCH-PIPELINE/utility/logging.py
UTILITY_DIR = os.path.dirname(os.path.abspath(__file__))

# 2. Path to project root: .../MLOPS-PYTORCH-PIPELINE/
PROJECT_ROOT = os.path.dirname(UTILITY_DIR)

# 3. Path to logs folder: .../MLOPS-PYTORCH-PIPELINE/logs/
LOG_DIR = os.path.join(PROJECT_ROOT, "logs")

# Ensure logs directory exists
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = os.path.join(LOG_DIR, "pipeline.log")


def get_logger(name: str) -> logging.Logger:
    """
    Returns a configured logger with portable file and console handlers.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Prevent handler duplication across multiple imports
    if logger.hasHandlers():
        logger.handlers.clear()

    # ---- Console Handler ----
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_format = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )
    console_handler.setFormatter(console_format)

    # ---- File Handler (Rotates daily at midnight) ----
    file_handler = TimedRotatingFileHandler(
        LOG_FILE, when="midnight", interval=1, backupCount=5, encoding="utf-8"
    )
    file_handler.setLevel(logging.DEBUG)
    file_format = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(funcName)s | %(message)s"
    )
    file_handler.setFormatter(file_format)

    # Attach handlers
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger