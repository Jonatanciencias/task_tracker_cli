# src/utils.py
"""
future versions:
- Input validation functions (e.g., checking if a task ID is valid).
- File handling helpers (e.g., checking if the task file exists).
- Formatting utilities (e.g., formatting dates or task output).
"""
import os
import json

# File handling for tasks
def load_tasks(file_path):
    """Loads tasks from the specified JSON file."""
    if not os.path.exists(file_path):
        return []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except json.JSONDecodeError as e:
        print(f"Error: Failed to decode file {file_path}. The file may be corrupted.")
        print(f"Error loading tasks: {e}")
        return []

def save_tasks(file_path, tasks):
    """Saves tasks to the specified JSON file."""
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(tasks, file, indent=4)
    except json.JSONDecodeError as e:
        print(f"Error saving tasks: {e}")

# Task status validation
def validate_status(status, valid_statuses):
    """Validates if the provided status is one of the allowed statuses."""
    if status not in valid_statuses:
        print(f"Error: '{status}' is not a valid status. Valid statuses are: {', '.join(valid_statuses)}")
        return False
    return True

def show_help():
    """
    Displays the available commands in the CLI, with instructions on how to use the script.
    """
    help_message = """
    ****************************************
    *                                      *
    *   ████████╗ █████╗ ███████╗██╗  ██╗  *
    *   ╚══██╔══╝██╔══██╗██╔════╝██║  ██║  *
    *      ██║   ███████║███████╗███████║  *
    *      ██║   ██╔══██║╚════██║██╔══██║  *
    *      ██║   ██║  ██║███████║██║  ██║  *
    *      ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝  *
    *                                      *
    ****************************************
    *                                      *
    *      Task Tracker CLI  v1.0.0        *
    *  Keep track of your tasks easily!    *
    *                                      *
    ****************************************
    
    Commands:
    - add <description>         Add a new task.
    - list [status]             List all tasks or tasks with a specific status.
    - update <ID> <desc>        Update a task description.
    - delete <ID>               Delete a task.
    - new_status <ID> <status>  Change task status.
    Usage:
    - python -m src.cli <command> [options]

    Commands:
    - add <description>: Add a new task.
    - list: List all tasks.
    - update <ID> <description>: Update the task with the specified ID.
    - delete <ID>: Delete the task with the specified ID.
    - new_status <ID> <status>: Change the status of the task.

    Examples:
    - python -m src.cli add "Finish the report"
    - python -m src.cli list
    - python -m src.cli update 1 "Review the report"
    - python -m src.cli delete 1
    - python -m src.cli new_status 1 done
    """
    print(help_message)