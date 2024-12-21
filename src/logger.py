#  Logger is for the purpose that for any execution, that probably happens, we should be able to log those changes, infomation, excution in some files so that we can be able to track those changes.
import logging
import os
import datetime

LOG_FILE = f"{datetime.datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" #filename
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE ) #log file path
os.makedirs(logs_path, exist_ok=True) #keep on appending the files in this folder whenever we want to create the file.


LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE) #the entire log file path.


logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,  # Here we can change the log level to DEBUG, INFO, WARNING, ERROR, CRITICAL.
)

