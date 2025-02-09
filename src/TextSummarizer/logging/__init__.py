import logging
import os
import sys
from datetime import datetime

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

logs_dir = "logs"
logs_filepath = os.path.join(logs_dir, "running_logs.log")
os.makedirs(logs_dir, exist_ok = True)

logging.basicConfig(
    level = logging.INFO,
    format = logging_str,
    handlers = [
        logging.FileHandler(logs_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("TextSummarizerLogger")

if __name__ == "__main__":
    logger.info("Welcome to my Custom Logging!")