# Every execution that happens can be logged in here (Comprende!)

import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m%d%Y__%H%M%S')}.log"
log_path = os.path.join(os.getcwd(),"logs", LOG_FILE)
os.makedirs(os.path.dirname(log_path), exist_ok=True)

LOG_FILE_PATH=log_path


logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(levelname)s - %(message)s",
    level=logging.INFO,
)

if __name__=="__main__":
    logging.info("Logging has begun")


