import os
import sys
import logging


logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
#logging_str_time_based = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

log_dir = "logs"
#it will only have current logging info and will not logging 
#   based on time stamp (useful in saving space)
log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level= logging.INFO,
    format= logging_str,
    handlers=[logging.FileHandler(log_filepath),
              logging.StreamHandler(sys.stdout)])
logger = logging.getLogger("imgClf")
