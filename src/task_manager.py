import json
from datetime import datetime
import os

TASKS_FILE = 'tasks.json'

def load_tasks():
    """
    Carga las tareas desde un archivo JSON.
    """
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, 'r', encoding='utf-8') as file:
        return json.load(file)

def save_tasks(tasks):
    """
    Guarda las tareas en un archivo JSON.
    """
    with open(TASKS_FILE, 'w', encoding='utf-8') as file:
        json.dump(tasks, file, indent=4)

def add_task(description):
    """
    Añade una nueva tarea al archivo de tareas.
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
    Actualiza la descripción de una tarea.
    """
    tasks = load_tasks()
    task = next((task for task in tasks if task['id'] == task_id), None)

    if task:
        task['description'] = new_description
        task['updated_at'] = str(datetime.now())
        save_tasks(tasks)
        print(f'Tarea {task_id} actualizada exitosamente.')
    else:
        print(f'Error: No se encontró la tarea con ID {task_id}.')

def delete_task(task_id):
    """
    Elimina una tarea con el ID especificado.
    """
    tasks = load_tasks()
    tasks = [task for task in tasks if task['id'] != task_id]
    save_tasks(tasks)
    print(f'Tarea {task_id} eliminada exitosamente.')

def status_task(task_id, new_status):
    """
    Actualiza el estado de una tarea.
    """
    tasks = load_tasks()
    task = next((task for task in tasks if task['id'] == task_id), None)

    if task:
        task['status'] = new_status
        task['updated_at'] = str(datetime.now())
        save_tasks(tasks)
        print(f'Estado de la tarea {task_id} actualizado a {new_status}.')
    else:
        print(f'Error: No se encontró la tarea con ID {task_id}.')
