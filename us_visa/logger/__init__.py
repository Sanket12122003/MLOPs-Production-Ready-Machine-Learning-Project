import logging
import os
from from_root import from_root
from datetime import datetime

# Generate log filename with timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Define the directory for logs
log_dir = 'logs'

# Create the full path for the log file
logs_path = os.path.join(from_root(), log_dir, LOG_FILE)

# Create the log directory if it does not exist
os.makedirs(os.path.join(from_root(), log_dir), exist_ok=True)

# Configure logging
logging.basicConfig(
    filename=logs_path,
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,
)
