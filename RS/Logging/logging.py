import os
import logging
from logging.handlers import RotatingFileHandler
from Database.Connection.ping_connection import connection_logger
from Database.Delete.delete_docs import delete_logger
from Database.InsertOne.insert_one import insert_one_logger
from Database.InsertMany.insert_many import insert_many_logger
from Database.SearchOne.search_one import search_one_logger
from Database.SearchAll.search_all import search_all_logger
from Database.Modify.modify import modify_logger
from User.Registration.register import registration_logger
from User.Login.login import login_logger

def setup_logging(log_dir):
    """
    Set up logging for different components of the Route Solutions application.

    This function creates loggers and file handlers for connection, delete, insert_one,
    insert_many, search_one, search_all, modify, registration, and login components,
    configuring them to write log messages to rotating log files.

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

    # Configure search_one logger
    search_log_file = os.path.join(log_dir, "search_one_logger.log")
    search_handler = RotatingFileHandler(search_log_file, maxBytes=1024 * 1024, backupCount=5)
    search_handler.setFormatter(formatter)
    search_one_logger.addHandler(search_handler)

    # Configure search_all logger
    search_all_log_file = os.path.join(log_dir, "search_all_logger.log")
    search_all_handler = RotatingFileHandler(search_all_log_file, maxBytes=1024 * 1024, backupCount=5)
    search_all_handler.setFormatter(formatter)
    search_all_logger.addHandler(search_all_handler)

    # Configure modify logger
    modify_log_file = os.path.join(log_dir, "modify_logger.log")
    modify_handler = RotatingFileHandler(modify_log_file, maxBytes=1024 * 1024, backupCount=5)
    modify_handler.setFormatter(formatter)
    modify_logger.addHandler(modify_handler)

    # Configure registration logger
    registration_log_file = os.path.join(log_dir, "registration_logger.log")
    registration_handler = RotatingFileHandler(registration_log_file, maxBytes=1024 * 1024, backupCount=5)
    registration_handler.setFormatter(formatter)
    registration_logger.addHandler(registration_handler)

    # Configure login logger
    login_log_file = os.path.join(log_dir, "login_logger.log")
    login_handler = RotatingFileHandler(login_log_file, maxBytes=1024 * 1024, backupCount=5)
    login_handler.setFormatter(formatter)
    login_logger.addHandler(login_handler)
