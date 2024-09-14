""" Module for task management. """
import json
from datetime import datetime
import os

TASKS_FILE = 'tasks.json'

def load_tasks():
    """
    Load tasks from the specified file.

    Returns:
        list: A list of tasks loaded from the file.
    """
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, 'r', encoding='utf-8') as file:
        return json.load(file)

def save_tasks(tasks):
    """
    Save the given tasks to a file.
    Parameters:
    tasks (list): A list of tasks to be saved.
    Returns:
    None
    """
    with open(TASKS_FILE, 'w', encoding='utf-8') as file:
        json.dump(tasks, file, indent=4)

def add_task(description):
    """
    Adds a new task to the task manager.
    Parameters:
    - description (str): The description of the task.
    Returns:
    - dict: The newly added task.
    """  
    tasks = load_tasks()
    task_id = len(tasks) + 1
    task = {
        'id': task_id,
        'description': description,
        'status': 'to-do',
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
    - task_id (int): The ID of the task to be updated.
    - new_description (str): The new description for the task.
    Returns:
    None
    Raises:
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
    - task_id (int): The ID of the task to be deleted.
    Returns:
    - None
    Raises:
    - None
    """  
    tasks = load_tasks()
    tasks = [task for task in tasks if task['id'] != task_id]
    save_tasks(tasks)
    print(f'Task {task_id} deleted successfully.')

def status_task(task_id, new_status):
    """
    Updates the status of a task with the given task_id.
    Parameters:
    - task_id (int): The ID of the task to update.
    - new_status (str): The new status to assign to the task.
    Returns:
    None
    Prints the updated status of the task if it exists, otherwise prints an error message.
    """
    tasks = load_tasks()
    task = next((task for task in tasks if task['id'] == task_id), None)

    if task:
        task['status'] = new_status
        task['updated_at'] = str(datetime.now())
        save_tasks(tasks)
        print(f'Status of task {task_id} updated to {new_status}.')
    else:
        print(f'Error: Task with ID {task_id} not found.')
