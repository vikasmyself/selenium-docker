import inspect
import os
import logging

def customLogger(logLevel=logging.DEBUG):
    # Ensure the logs directory exists
    log_directory = "/Users/vmata/Documents/New_Sess/selenium-docker/logs"
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)

    # Get the name of the calling class/method
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)
    logger.setLevel(logging.DEBUG)

    # Check if the handler already exists to avoid duplicates
    if not logger.handlers:
        log_file = os.path.join(log_directory, "automation.log")
        fileHandler = logging.FileHandler(log_file, mode='w')
        fileHandler.setLevel(logLevel)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                                      datefmt='%m/%d/%Y %I:%M:%S %p')
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)

    return logger

# Example usage
# log = customLogger()
# log.info("This is an info message")
