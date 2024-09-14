""" Módulo para la gestión de tareas. """
from datetime import datetime
from .utils import load_tasks, save_tasks, validate_status

TASKS_FILE = 'tasks.json'
VALID_STATUSES = ['to-do', 'in-progress', 'completed']

def add_task(description):
    """
    Adds a new task to the task manager.
    Parameters:
    - description (str): The description of the task.
    Returns:
    - dict: The newly created task.
    """

    tasks = load_tasks(TASKS_FILE)
    task_id = len(tasks) + 1
    task = {
        'id': task_id,
        'description': description,
        'status': 'to-do',
        'created_at': str(datetime.now()),
        'updated_at': str(datetime.now())
    }
    tasks.append(task)
    save_tasks(TASKS_FILE, tasks)
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

    tasks = load_tasks(TASKS_FILE)
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task:
        task['description'] = new_description
        task['updated_at'] = str(datetime.now())
        save_tasks(TASKS_FILE, tasks)
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

    tasks = load_tasks(TASKS_FILE)
    tasks = [task for task in tasks if task['id'] != task_id]
    save_tasks(TASKS_FILE, tasks)
    print(f'Task {task_id} deleted successfully.')

def status_task(task_id, new_status):
    """
    Updates the status of a task with the given task_id.
    Parameters:
        task_id (int): The ID of the task to update.
        new_status (str): The new status to assign to the task.
    Returns:
        None
    Raises:
        None
    """

    if not validate_status(new_status, VALID_STATUSES):
        return

    tasks = load_tasks(TASKS_FILE)
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task:
        task['status'] = new_status
        task['updated_at'] = str(datetime.now())
        save_tasks(TASKS_FILE, tasks)
        print(f'Status of task {task_id} updated to {new_status}.')
    else:
        print(f'Error: Task with ID {task_id} not found.')
