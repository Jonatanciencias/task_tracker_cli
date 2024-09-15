""" Task Management Module """
# src/task_manager.py

import os
from datetime import datetime
import logging
from .utils import load_tasks, save_tasks, validate_status  # Import validate_status from utils.py

# Determine the root directory dynamically (e.g., virtual environment)
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Default task file in the root of the virtual environment
TASKS_FILE = os.path.join(ROOT_DIR, 'tasks.json')

# Valid statuses for the tasks
VALID_STATUSES = ['to-do', 'in-progress', 'done']

# Set the path for the logs directory inside the root directory
LOG_DIR = os.path.join(ROOT_DIR, 'logs')

# Ensure the logs directory exists
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

LOG_FILE = os.path.join(LOG_DIR, 'task_manager.log')

# Configure logging to the logs directory
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode='a'  # Use 'a' to append logs
)

def add_task(description, file_path=TASKS_FILE):
    """
    Adds a new task to the task manager.
    Parameters:
    - description (str): The description of the task.
    - file_path (str): Optional path to the tasks file.
    Returns:
    - dict: The newly created task.
    """
    tasks = load_tasks(file_path)
    task_id = len(tasks) + 1
    task = {
        'id': task_id,
        'description': description,
        'status': 'to-do',
        'created_at': str(datetime.now()),
        'updated_at': str(datetime.now())
    }
    tasks.append(task)
    save_tasks(file_path, tasks)
    logging.info("Task added: %s", task)
    return task

def update_task(task_id, new_description, file_path=TASKS_FILE):
    """
    Updates the description of a task with the given task_id.
    Parameters:
    - task_id (int): The ID of the task to update.
    - new_description (str): The new description for the task.
    - file_path (str): Optional path to the tasks file.
    Returns:
    - None
    """
    tasks = load_tasks(file_path)
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task:
        task['description'] = new_description
        task['updated_at'] = str(datetime.now())
        save_tasks(file_path, tasks)
        logging.info('Task %s updated successfully.', task_id)
    else:
        logging.error('Task with ID %s not found.', task_id)
        raise ValueError(f'Task with ID {task_id} not found.')

def delete_task(task_id, file_path=TASKS_FILE):
    """
    Deletes a task with the given task_id from the task manager.
    Parameters:
    - task_id (int): The ID of the task to be deleted.
    - file_path (str): Optional path to the tasks file.
    Returns:
    - None
    """
    tasks = load_tasks(file_path)
    tasks = [task for task in tasks if task['id'] != task_id]
    save_tasks(file_path, tasks)
    logging.info('Task %s deleted successfully.', task_id)

def status_task(task_id, new_status, file_path=TASKS_FILE):
    """
    Updates the status of a task with the given task_id.
    Parameters:
    - task_id (int): The ID of the task to update.
    - new_status (str): The new status to assign to the task.
    - file_path (str): Optional path to the tasks file.
    Returns:
    - None
    """
    # Use validate_status from utils.py
    if not validate_status(new_status):  # No need to pass VALID_STATUSES
        logging.error("Invalid status '%s'.", new_status)
        raise ValueError(f"Invalid status '{new_status}'. Valid statuses are: {', '.join(VALID_STATUSES)}")

    tasks = load_tasks(file_path)
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task:
        task['status'] = new_status
        task['updated_at'] = str(datetime.now())
        save_tasks(file_path, tasks)
        logging.info('Status of task %s updated to %s.', task_id, new_status)
    else:
        logging.error('Task with ID %s not found.', task_id)
        raise ValueError(f'Task with ID {task_id} not found.')
