"""Task Manager Package"""
# src/__init__.py

import os
import logging
import json

# Import functions from task_manager
from .task_manager import (
    load_tasks,
    add_task,
    update_task,
    delete_task,
    status_task
)

# Set the path to the root directory and tasks.json file
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
task_file_path = os.path.join(root_dir, 'tasks.json')

# Set up the logs directory and log file
LOG_DIR = os.path.join(root_dir, 'logs')
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# Set up logging configuration to log only to the file, not the console
log_file = os.path.join(LOG_DIR, 'app.log')
logging.basicConfig(
    filename=log_file,  # Log only to the file
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode='w'  # Overwrites the log file every time (use 'a' to append)
)

logger = logging.getLogger(__name__)

# Metadata for the package
__version__ = "2.0.0"
__author__ = "Jonatan Garcia"
__license__ = "MIT"

# Function to check the existence of tasks.json
def check_task_file():
    """
    Verifies if the tasks.json file exists. If not, creates it in the root of the project.
    """
    if not os.path.exists(task_file_path):
        logger.info("tasks.json file does not exist in %s. Creating a new one...", root_dir)
        with open(task_file_path, 'w', encoding='utf-8') as f:
            json.dump([], f)  # Create an empty JSON array to store tasks
            logger.info("Created a new tasks.json file at %s", task_file_path)
    else:
        logger.info("tasks.json file found at %s", task_file_path)

    return task_file_path  # Return the path to be used in load_tasks and other operations

# Call the function to check the file on initialization and load tasks
task_file_path = check_task_file()
tasks = load_tasks(file_path=task_file_path)
logger.info("Tasks loaded: %s", tasks)
