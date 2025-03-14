import logging
from os import path, makedirs

from datetime import datetime
from app.settings import config

# Define the base log directory
log_base_folder = config['LOG_DIR']

# Generate a subfolder for the current date
current_date = datetime.now().strftime('%d-%m-%Y')
date_folder = path.join(log_base_folder, current_date)
if not path.exists(date_folder):
    makedirs(date_folder)

# Generate the log file name with the current time
log_filename = path.join(date_folder, f"{datetime.now().strftime('%H-%M-%S')}.log")

# Set up the logger
def setup_logger(name: str='logger'):
    custom_logger = logging.getLogger(name)
    custom_logger.setLevel(logging.DEBUG)  # Set the default logging level

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
    custom_logger.addHandler(file_handler)
    custom_logger.addHandler(console_handler)

    return custom_logger

logger = setup_logger()
