# src/cli.py

import sys
from task_manager import load_tasks, save_tasks, add_task, list_tasks, update_task, delete_task, status_task

def show_help():
    help_message = """
    Task Tracker CLI:
    
    Comandos:
    - add <descripcion>: Add new task.
    - list: List all tasks.
    - update <ID> <descripcion>: Update a task with a specific ID.
    - delete <ID>: Delete a task with a specific ID.
    - new_status <ID> <status>: Change the task's status.
    """
    print(help_message)

def main():
    pass

if __name__ == '__main__':
    main()