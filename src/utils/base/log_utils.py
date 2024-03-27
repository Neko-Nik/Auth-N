"""
This module contains utility functions for logging.
This will be used to configure the logger for the application.
"""

import logging
import time
import traceback
from pythonjsonlogger import jsonlogger
from logging.handlers import RotatingFileHandler


class CustomJsonFormatter(jsonlogger.JsonFormatter):
    """Custom formatter for logging in JSON format"""
    def formatTime(self, record, datefmt=None):
        """Format the time in the log record"""
        ct = time.localtime(record.created)
        if datefmt:
            formatted_time = time.strftime(datefmt, ct)
        else:
            formatted_time = time.strftime(self.default_time_format, ct)
        return f"{formatted_time}.{record.msecs:03.0f}"

    def add_fields(self, log_record, record, message_dict):
        """Add custom fields to the log record"""
        super(CustomJsonFormatter, self).add_fields(log_record, record, message_dict)
        if record.exc_info:
            exception_text = traceback.format_exception(*record.exc_info)
            log_record['exception'] = exception_text




def configure_return_logger(LOG_LEVEL, LOG_FILE_PATH):
    """Configure the logger and return it"""
    log_formatter = CustomJsonFormatter("%(asctime)s %(levelname)s %(module)s - %(funcName)s: %(message)s")

    # Configure the log handler
    log_handler = RotatingFileHandler(LOG_FILE_PATH, maxBytes=1024*1024*1024, backupCount=10)
    log_handler.setLevel(LOG_LEVEL)
    log_handler.setFormatter(log_formatter)

    # Initialize the logger
    logger = logging.getLogger("NekoNik-Logs")
    logger.setLevel(LOG_LEVEL)
    logger.addHandler(log_handler)
    logger.debug(f"Logging initialized at level {LOG_LEVEL}")

    return logger
