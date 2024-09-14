"""" Module for task management. """
import json
from datetime import datetime
import os

# Define constants for the tasks file and possible states
TASKS_FILE = os.path.join(os.path.dirname(__file__), 'tasks.json')

# Define possible task states
TO_DO = 'to-do'
IN_PROGRESS = 'in-progress'
COMPLETED = 'completed'

def load_tasks():
    """
    Load tasks from the specified file.

    Returns:
        list: A list of tasks loaded from the file. If the file doesn't exist, returns an empty list.
    """
    if not os.path.exists(TASKS_FILE):
        return []
    
    try:
        with open(TASKS_FILE, 'r', encoding='utf-8') as file:
            return json.load(file)
    except json.JSONDecodeError:
        print(f"Error: Failed to decode file {TASKS_FILE}. The file may be corrupted.")
        return []
    except FileNotFoundError as e:
        print(f"Error loading tasks: {e}")
        return []

def save_tasks(tasks):
    """
    Save the given tasks to a file.

    Parameters:
        tasks (list): A list of tasks to be saved.

    Returns:
        None
    """
    try:
        with open(TASKS_FILE, 'w', encoding='utf-8') as file:
            json.dump(tasks, file, indent=4)
    except FileNotFoundError as e:
        print(f"Error saving tasks: {e}")

def add_task(description):
    """
    Adds a new task to the task manager.

    Parameters:
        description (str): The description of the task.

    Returns:
        dict: The newly added task.
    """
    tasks = load_tasks()
    task_id = len(tasks) + 1
    task = {
        'id': task_id,
        'description': description,
        'status': TO_DO,
        'created_at': str(datetime.now()),
        'updated_at': str(datetime.now())
    }
    tasks.append(task)
    save_tasks(tasks)
    return task

def update_task(task_id, new_description):
    """
    Update the description of a task with the given task_id.

    Parameters:
        task_id (int): The ID of the task to be updated.
        new_description (str): The new description for the task.

    Returns:
        None
    """
    tasks = load_tasks()
    task = next((task for task in tasks if task['id'] == task_id), None)

    if task:
        task['description'] = new_description
        task['updated_at'] = str(datetime.now())
        save_tasks(tasks)
        print(f'Task {task_id} updated successfully.')
    else:
        print(f'Error: Task with ID {task_id} not found.')

def delete_task(task_id):
    """
    Deletes a task with the given task_id from the task manager.

    Parameters:
        task_id (int): The ID of the task to be deleted.

    Returns:
        None
    """
    tasks = load_tasks()
    initial_len = len(tasks)
    tasks = [task for task in tasks if task['id'] != task_id]
    
    if len(tasks) < initial_len:
        save_tasks(tasks)
        print(f'Task {task_id} deleted successfully.')
    else:
        print(f'Error: Task with ID {task_id} not found.')

def status_task(task_id, new_status):
    """
    Updates the status of a task with the given task_id.

    Parameters:
        task_id (int): The ID of the task to update.
        new_status (str): The new status to assign to the task.

    Returns:
        None
    """
    valid_statuses = [TO_DO, IN_PROGRESS, COMPLETED]

    if new_status not in valid_statuses:
        print(f"Error: '{new_status}' is not a valid state. Valid states are: {', '.join(valid_statuses)}")
        return

    tasks = load_tasks()
    task = next((task for task in tasks if task['id'] == task_id), None)

    if task:
        task['status'] = new_status
        task['updated_at'] = str(datetime.now())
        save_tasks(tasks)
        print(f'Status of task {task_id} updated to {new_status}.')
    else:
        print(f'Error: Task with ID {task_id} not found.')
