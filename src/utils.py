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
