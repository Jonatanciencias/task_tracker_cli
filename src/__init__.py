""""Task Manager Package"""

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

# Set up logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Metadata for the package
__version__ = "1.0.0"
__author__ = "Jonatan Garcia"
__license__ = "MIT"

# Function to check the existence of tasks.json
def check_task_file():
    """
    Verifies if the tasks.json file exists. If not, creates it in the root of the project.
    """
    # Set the path to the root directory and tasks.json file
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))  # Root directory of the project
    task_file_path = os.path.join(root_dir, 'tasks.json')  # Path to tasks.json in the root

    if not os.path.exists(task_file_path):
        logger.info(f"tasks.json file does not exist in {root_dir}. Creating a new one...")
        with open(task_file_path, 'w', encoding='utf-8') as f:
            json.dump([], f)  # Create an empty JSON array to store tasks

    return task_file_path  # Return the path to be used in load_tasks and other operations

# Call the function to check the file on initialization and load tasks
task_file_path = check_task_file()
tasks = load_tasks(file_path=task_file_path)
