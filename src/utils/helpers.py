# Utility functions
import logging
import sys
from datetime import datetime

# Configure basic logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler("mlops.log")
    ]
)

def log_info(message):
    logging.info(message)

def log_error(message):
    logging.error(message)

def timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")