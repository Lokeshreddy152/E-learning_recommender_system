import logging
import os
import sys
from datetime import datetime

# Define the directory for log files
LOG_DIR = "logs"
LOG_DIR = os.path.join(os.getcwd(), LOG_DIR)  # Create a full path to the log directory

# Create the log directory if it doesn't exist
os.makedirs(LOG_DIR, exist_ok=True)

# Get the current timestamp in the format 'YYYY-MM-DD-HH-MM-SS'
CURRENT_TIME_STAMP = f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"

# Define the log file name using the timestamp
file_name = f"log_{CURRENT_TIME_STAMP}.log"

# Create the full path to the log file
log_file_path = os.path.join(LOG_DIR, file_name)

# Configure the logging system
logging.basicConfig(
    filename=log_file_path,  # Specify the log file path
    filemode="w",  # Use "w" to overwrite the log file if it exists
    format='[%(asctime)s] %(name)s - %(levelname)s - %(message)s',  # Define the log message format
    level=logging.INFO  # Set the logging level to INFO
)