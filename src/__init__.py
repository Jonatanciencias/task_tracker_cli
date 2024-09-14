"""Task Manager Package"""

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
# Function to check the existence of tasks.json
def check_task_file():
    """
    Verifies if the tasks.json file exists. If not, creates it.
    """
    # Cambia esta ruta para apuntar siempre a la raíz del proyecto
    task_file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'tasks.json')
    
    if not os.path.exists(task_file_path):
        logger.info("tasks.json file does not exist. Creating a new one...")
        with open(task_file_path, 'w', encoding='utf-8') as f:
            json.dump([], f)

# Call the function to check the file on initialization
check_task_file()

# Load tasks when the package is imported
tasks = load_tasks(file_path=os.path.join(os.path.dirname(os.path.dirname(__file__)), 'tasks.json'))
