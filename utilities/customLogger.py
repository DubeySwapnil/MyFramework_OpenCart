import logging
import os
import msvcrt
from selenium.webdriver.remote.remote_connection import LOGGER as selenium_logger


class LogGen:
    @staticmethod
    def loggen(clear_log=True):
        if clear_log:
            LogGen.clear_log_file()

        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(funcName)s() - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

        log_path = os.path.abspath(os.path.join(os.curdir, 'logs', 'automation.log'))
        os.makedirs(os.path.dirname(log_path), exist_ok=True)  # Create logs directory if it doesn't exist
        file_handler = logging.FileHandler(log_path)
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

        # Configure Selenium logger to capture browser logs
        selenium_logger.setLevel(logging.DEBUG)
        selenium_logger.addHandler(file_handler)

        return logger

    @staticmethod
    def clear_log_file():
        log_path = os.path.abspath(os.path.join(os.curdir, 'logs', 'automation.log'))
        if os.path.exists(log_path):
            with open(log_path, 'a'):
                pass  # This will create the file if it doesn't exist or truncate it if it does
