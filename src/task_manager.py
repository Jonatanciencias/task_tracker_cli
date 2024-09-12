# src/task_manager.py

import json
from datetime import datetime
import os


TASK_FILE = 'tasks.json'

def load_tasks():
    """1. Load tasks from json file"""
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASKS_FILE, 'r') as file:
        tasks = json.load(file)

def save_tasks(tasks):
    """2. Save tasks to json file"""
    with open(TASK_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task(description):
    """3. Add a new task to json file"""
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
    """4. List all tasks"""
    tasks = load_tasks()
    if tasks:
        for task in tasks:
            print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}")
    else:
        print("No tasks found")

def update_task(task_id, new_description):
    pass

def delete_task(task_id):
    pass

def status_task(task_id):
    pass