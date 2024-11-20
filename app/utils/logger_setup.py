import logging
from os import path, makedirs
from datetime import datetime
from .settings import config


# Create a logs folder if it doesn't exist
log_folder = config['LOG_DIR']
if not path.exists(log_folder):
    makedirs(log_folder)

# Generate a log file name with the current date
log_filename = path.join(log_folder, f"{datetime.now().strftime('%Y-%m-%d')}.log")

# Set up the logger
def setup_logger(name: str='logger'):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)  # Set the default logging level

    # Create handlers for file and console logging
    file_handler = logging.FileHandler(log_filename)
    console_handler = logging.StreamHandler()

    # Set the level for each handler
    file_handler.setLevel(logging.DEBUG)
    console_handler.setLevel(logging.INFO)

    # Define a logging format
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

logger = setup_logger()
