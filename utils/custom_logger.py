import inspect
import os
import logging


def customLogger(logLevel=logging.DEBUG):
    # Ensure the logs directory exists
    if not os.path.exists("./logs"):
        os.makedirs("./logs")

    # Get the name of the calling class/method
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)
    logger.setLevel(logging.DEBUG)

    # Check if the handler already exists to avoid duplicates
    if not logger.handlers:
        fileHandler = logging.FileHandler("selenium-docker/logs/automation.log", mode='w')
        fileHandler.setLevel(logLevel)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                                       datefmt='%m/%d/%Y %I:%M:%S %p')
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)

    return logger
