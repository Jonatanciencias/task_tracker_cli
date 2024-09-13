# src/task_manager.py

import json
from datetime import datetime
import os


TASKS_FILE = 'tasks.json'

def load_tasks():
    """
    Load tasks from a file.
    Returns:
        list: A list of tasks loaded from the file.
    Raises:
        IOError: If there is an error while loading the tasks file.
        json.JSONDecodeError: If there is an error decoding the JSON data from the file.
    """

    try:
        if not os.path.exists(TASKS_FILE):
            return []
        with open(TASKS_FILE, 'r', encoding='utf-8') as file:
            return json.load(file)
    except (IOError, json.JSONDecodeError) as e:
        print(f"Error loading tasks: {e}")
        return []

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

def list_tasks():
    """
    Prints the list of tasks.

    This function loads the tasks from the task manager and prints them in the following format:
    ID: <task_id>, Description: <task_description>, Status: <task_status>

    If no tasks are found, it prints "No tasks found".
    """
    tasks = load_tasks()
    if tasks:
        for task in tasks:
            print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}")
    else:
        print("No tasks found")

def update_task(task_id, new_description):
    """
    Update the description of a task with the given task_id.
    Parameters:
    - task_id (int): The ID of the task to be updated.
    - new_description (str): The new description for the task.
    Returns:
    - None
    Raises:
    - None
    """
    tasks = load_tasks() # Load all tasks from file
    task = next((task for task in tasks if task['id'] == task_id), None)  # search task by ID

    if not task:
        print(f"Error: No task found with ID {task_id}")
        return

    # If the task is found, update the description and the updated_at field
    task['description'] = new_description
    task['updatedAt'] = str(datetime.now())
    save_tasks(tasks)
    print(f'Task: {task_id} updated sucefully.')

def delete_task(task_id):
    """
    Deletes a task with the given task_id from the task manager.
    Args:
        task_id (int): The ID of the task to be deleted.
    Returns:
        None
    Raises:
        None
    """
    tasks = load_tasks()
    task = next((task for task in tasks if task['id'] == task_id), None)  # search task by ID

    if not task:
        print(f"Error: No task found with ID {task_id}")
        return

    # If the task is found, remove it from the list of tasks and save the updated list
    tasks = [task for task in tasks if task['id'] != task_id]
    save_tasks(tasks)
    print(f'Task: {task_id} sucefully deleted.')

def status_task(task_id, new_status):
    """
    Update the status of a task.
    Parameters:
    - task_id (int): The ID of the task to update.
    - new_status (str): The new status to assign to the task.
    Returns:
    - None
    Raises:
    - None
    Description:
    - This function updates the status of a task identified by its ID. It first loads all the tasks from the task manager,
      then validates that the provided status is valid. If the status is not valid, an error message is printed and the function returns.
      If the provided task ID is not found in the list of tasks, an error message is printed and the function returns.
      If the provided task ID is found, the status of the task is updated to the new status and the 'updatedAt' field is updated with the current datetime.
      Finally, the updated list of tasks is saved and a success message is printed.
    Example:
    - status_task(1, 'in-progress')
    """
    tasks = load_tasks()
    valid_statuses = ['to-do', 'in-progress', 'done']

    # Validate that the provided status is valid
    if new_status not in valid_statuses:
        print(f"Error: Invalid status. Use one of the following: {', '.join(valid_statuses)}")
        return

    task = next((task for task in tasks if task['id'] == task_id), None)

    if not task:
        print(f"Error: No task found with ID {task_id}.")
        return

    # If the ID is valid, update the status
    task['status'] = new_status
    task['updatedAt'] = str(datetime.now())
    save_tasks(tasks)
    print(f"Task {task_id} status successfully updated to '{new_status}'.")
