import logging
from enum import Enum 
class LogLevel(Enum):

    CRITICAL = 50
    ERROR = 40
    WARNING = 30
    INFO = 20
    DEBUG = 10
    NOTSET = 0

LOGGER_FILE_NAME = "randomm.log" #путь логгера
LOGGER_LEVEL = LogLevel.INFO # = 50
LOGGER_FORMATTER = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s') # форма записи в файл

logger = logging.getLogger("Рандом")
logger.setLevel(LOGGER_LEVEL.value) 

file_handler = logging.FileHandler(LOGGER_FILE_NAME, 'a', 'utf-8') 
file_handler.setLevel(LOGGER_LEVEL.value) 
file_handler.setFormatter(LOGGER_FORMATTER) #форма записи 
logger.addHandler(file_handler)

def log_message(log_level: LogLevel, message: str):
    logger.log(log_level.value, message)
