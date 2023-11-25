import os
import logging
from logging.handlers import RotatingFileHandler
from Database.Connection.ping_connection import connection_logger
from Database.Delete.delete_docs import delete_logger
from Database.InsertOne.insert_one import insert_one_logger
from Database.InsertMany.insert_many import insert_many_logger

def setup_logging(log_dir):
    """
    Set up logging for different components of the Route Solutions application.

    This function creates loggers and file handlers for connection, delete, insert_one,
    and insert_many components, configuring them to write log messages to rotating log files.

    Parameters:
    - log_dir (str): The directory where log files will be stored.
    """

    # Ensure the log directory exists
    os.makedirs(log_dir, exist_ok=True)

    # Define a common log message format
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    # Configure connection logger
    connection_log_file = os.path.join(log_dir, "connection_logger.log")
    connection_handler = RotatingFileHandler(connection_log_file, maxBytes=1024 * 1024, backupCount=5)
    connection_handler.setFormatter(formatter)
    connection_logger.addHandler(connection_handler)

    # Configure delete logger
    delete_log_file = os.path.join(log_dir, "delete_logger.log")
    delete_handler = RotatingFileHandler(delete_log_file, maxBytes=1024 * 1024, backupCount=5)
    delete_handler.setFormatter(formatter)
    delete_logger.addHandler(delete_handler)

    # Configure insert_one logger
    insert_one_logger_log_file = os.path.join(log_dir, "insert_one_logger.log")
    insert_one_handler = RotatingFileHandler(insert_one_logger_log_file, maxBytes=1024 * 1024, backupCount=5)
    insert_one_handler.setFormatter(formatter)
    insert_one_logger.addHandler(insert_one_handler)

    # Configure insert_many logger
    insert_many_logger_log_file = os.path.join(log_dir, "insert_many_logger.log")
    insert_many_handler = RotatingFileHandler(insert_many_logger_log_file, maxBytes=1024 * 1024, backupCount=5)
    insert_many_handler.setFormatter(formatter)
    insert_many_logger.addHandler(insert_many_handler)
