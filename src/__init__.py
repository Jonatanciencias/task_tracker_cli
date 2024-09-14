# src/__init__.py

""" Task Manager Package"""

# Task system initialization
import os
import logging
import json

# Import functions from cli
from .cli import main, show_help

# Import functions from utils (if you have any implemented)
from .utils import some_utility_function  # If there is any specific utility

# Package metadata
__version__ = "1.0.0"
__author__ = "Jonatan Garcia"
__license__ = "MIT"

# Import functions from task_manager
from .task_manager import (
    load_tasks,
    add_task,
    update_task,
    delete_task,
    status_task
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def check_task_file():
    """Check the existence of tasks.json and create it if it doesn't exist"""
    task_file_path = os.path.join(os.path.dirname(__file__), 'tasks.json')
    if not os.path.exists(task_file_path):
        logger.info("The tasks.json file does not exist. Creating a new one...")
        with open(task_file_path, 'w', encoding='utf-8') as f:
            json.dump([], f)

check_task_file()

# Load tasks on startup
tasks = load_tasks()
