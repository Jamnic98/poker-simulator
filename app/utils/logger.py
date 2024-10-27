import logging


logger = logging.getLogger('logging')
logger.setLevel(logging.INFO)
# create a formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# Create a file handler
file_handler = logging.FileHandler('logs.txt')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# if config["ENV"] != 'production':
#     # Create a stream handler for console output
#     console_handler = logging.StreamHandler()
#     console_handler.setLevel(logging.INFO)
#     console_handler.setFormatter(formatter)
#     logger.addHandler(console_handler)
