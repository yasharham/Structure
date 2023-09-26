import datetime
import os
import logging.config
from pydantic import BaseModel
from Utils.V1.utility_functions import getPath

from datetime import date
import traceback
from logging.handlers import RotatingFileHandler,TimedRotatingFileHandler
from Utils.V1.config_reader import configure




# def checkIfDirectoryExists(path):
#     try:
#         if not os.path.exists(path):
#             os.mkdir(path)
#         return path
#     except:
#         print(traceback.print_exc())
#


class LogConfig(BaseModel):
    LOGGER_NAME: str = "compliancelogger"
    LOG_FORMAT: str = "%(levelprefix)s | %(asctime)s | %(funcName)s | %(message)s"
    LOG_LEVEL: str = "DEBUG"
    LOG_FILE_MAX_SIZE_BYTES = 5 * 1024 *1024  # 5 MB
    LOG_FILE_PATH = os.path.join(getPath('LOGGER_PATH'), "scangreeks.log")

    # Logging config
    version = 1
    disable_existing_loggers = False
    formatters = {
        "default": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": LOG_FORMAT,
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    }


    handlers = {
        "default": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stderr",
        },
        # "size_rotating_file": {
        #     "formatter": "default",
        #     "class": "logging.handlers.RotatingFileHandler",
        #     "filename": os.path.join(file_path, f"scangreeks_{date}.log"),  # Specify the file name for logs
        #     "maxBytes": LOG_FILE_MAX_SIZE_BYTES,  # 5MB file size limit
        #     "backupCount" : 3,  # Number of backup log files to keep
        # },

        "TimedRotatingFileHandler":{
            "formatter": "default",
            "class": "logging.handlers.TimedRotatingFileHandler",
            "filename": LOG_FILE_PATH,  # Specify the file name for logs
            "when":'midnight',
            "backupCount":0,
        }


    }
    loggers = {
        LOGGER_NAME: {"handlers": ["default","TimedRotatingFileHandler"], "level": LOG_LEVEL},
    }


logging.config.dictConfig(LogConfig().dict())

logger = logging.getLogger('compliancelogger')
