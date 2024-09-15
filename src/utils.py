""" Utility functions for the Task Tracker CLI application. """
# src/utils.py

import os
import json
import logging

# Set up the log directory and file
LOG_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'logs')
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

LOG_FILE = os.path.join(LOG_DIR, 'utils.log')
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
)

# File handling for tasks
def load_tasks(file_path):
    """Loads tasks from the specified JSON file."""
    logging.info("Loading tasks from: %s", file_path)
    if not os.path.exists(file_path):
        logging.warning("File not found at %s. Creating an empty one.", file_path)
        return []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            tasks = json.load(file)
            logging.info("Loaded tasks: %s", tasks)
            return tasks
    except json.JSONDecodeError as e:
        logging.error("Failed to decode file %s. The file may be corrupted. Error: %s", file_path, e)
        return []

def save_tasks(file_path, tasks):
    """Saves tasks to the specified JSON file."""
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(tasks, file, indent=4)
            logging.info("Tasks saved successfully to %s.", file_path)
    except FileNotFoundError as e:
        logging.error("Failed to save tasks to %s. Error: %s", file_path, e)

# Task status validation
VALID_STATUSES = ['to-do', 'in-progress', 'done']

def validate_status(status):
    """Validates if the provided status is one of the allowed statuses."""
    if status not in VALID_STATUSES:
        logging.error("Invalid status '%s'. Valid statuses are: %s", status, ', '.join(VALID_STATUSES))
        return False
    logging.info("Status '%s' is valid.", status)
    return True

# Helper functions
def show_help():
    """
    Displays the available commands in the CLI, with instructions on how to use the script.
    """
    help_message = """
    **************************************************
    *                                                *
    *  88888888888     d8888  .d8888b.  888    d8P   *
    *      888        d88888 d88P  Y88b 888   d8P    *
    *      888       d88P888 Y88b.      888  d8P     *
    *      888      d88P 888  "Y888b.   888d88K      *
    *      888     d88P  888     "Y88b. 8888888b     *
    *      888    d88P   888       "888 888  Y88b    *
    *      888   d8888888888 Y88b  d88P 888   Y88b   *
    *      888  d88P     888  "Y8888P"  888    Y88b  *
    *                                                *
    **************************************************
    *                                                *
    *             Task Tracker CLI  v2.0.0           *
    *          Keep track of your tasks easily!      *
    *                                                *
    **************************************************
    
    Commands:
    - task-cli add <description>         Add a new task.
    - task-cli list [status]             List all tasks or tasks with a specific status.
    - task-cli update <ID> <desc>        Update a task description.
    - task-cli delete <ID>               Delete a task.
    - task-cli new_status <ID> <status>  Change task status.
    
    Usage:
    - task-cli <command> [options]

    Examples:
    - task-cli add "Finish the report"
    - task-cli list
    - task-cli list done
    - task-cli update 1 "Review the report"
    - task-cli delete 1
    - task-cli new_status 1 done
    """
    logging.info("Help message displayed.")
    print(help_message)
