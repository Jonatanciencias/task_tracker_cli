# src/task_manager.py

import json
from datetime import datetime
import os


TASK_FILE = 'tasks.json'

def load_tasks():
    """
    Load tasks from a file.

    Returns:
        list: A list of tasks loaded from the file.
    """

    if not os.path.exists(TASK_FILE):
        return []
    with open(TASKS_FILE, 'r') as file:
        tasks = json.load(file)

def save_tasks(tasks):
    """
    Save the given tasks to a file.
    Parameters:
    tasks (list): A list of tasks to be saved.
    Returns:
    None
    """

    with open(TASK_FILE, 'w') as file:
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
    Updates the description of a task with the given task_id.

    Parameters:
    - task_id (int): The ID of the task to be updated.
    - new_description (str): The new description for the task.

    Returns:
    None

    Prints a success message if the task is updated successfully.
    Prints an error message if no task is found with the given task_id.
    """
    tasks = load_tasks() 
    for task in tasks:
        if task['id'] == task_id:
            task['description'] = new_description 
            task['updatedAt'] = str(datetime.now()) 
            save_tasks(tasks) 
            print(f'Tarea {task_id} actualizada exitosamente.')
            return
    print(f'No se encontro una tarea con ID {task_id}.')


def delete_task(task_id):
    pass

def status_task(task_id):
    pass