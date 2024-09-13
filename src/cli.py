import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.task_manager import load_tasks, add_task, update_task, delete_task, status_task


def show_help():
    """
    Displays the help message for Task Tracker CLI, outlining the available commands and their usage.
    """
    help_message = """
    Task Tracker CLI:

    Commands:
    - add <description>: Adds a new task with the given description.
    - list: Lists all tasks.
    - update <ID> <description>: Updates the task with the specified ID and new description.
    - delete <ID>: Deletes the task with the given ID.
    - new_status <ID> <status>: Changes the status of the task with the given ID.

    Examples:
    - add: task-cli add "Finish documentation"
    - list: task-cli list
    - update: task-cli update 123 "Finish testing"
    - delete: task-cli delete 123
    - new_status: task-cli new_status 123 done
    """
    print(help_message)


def main():
    """
    Entry point of the Task Tracker CLI application.

    Parses command-line arguments and executes the corresponding commands:
    - add: Adds a new task with a description.
    - list: Lists all tasks with their IDs, descriptions, and statuses.
    - update: Updates the description of a task by its ID.
    - delete: Deletes a task by its ID.
    - new_status: Updates the status of a task by its ID.

    Examples:
    - task-cli add "Complete project"
    - task-cli list
    - task-cli update 1 "Update project description"
    - task-cli delete 1
    - task-cli new_status 1 done
    """
    if len(sys.argv) < 2:
        show_help()
        return

    # Determine the command to execute based on user input
    command = sys.argv[1]

    if command == 'add':
        # Check if the description is provided for the 'add' command
        if len(sys.argv) < 3:
            print("Usage: task-cli add <description>")
        else:
            description = ' '.join(sys.argv[2:])
            task = add_task(description)
            print(f"Task added successfully: {task['id']}")

    elif command == 'list':
        # Load and display all tasks
        tasks = load_tasks()
        if tasks:
            for task in tasks:
                print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}")
        else:
            print("No tasks found")

    elif command == 'update':
        # Check if task ID and new description are provided
        if len(sys.argv) < 4:
            print("Use: task-cli update <ID> <new description>")
        else:
            task_id = int(sys.argv[2])
            new_description = " ".join(sys.argv[3:])
            update_task(task_id, new_description)

    elif command == 'delete':
        # Check if task ID is provided
        if len(sys.argv) < 3:
            print("Use: task-cli delete <ID>")
        else:
            task_id = int(sys.argv[2])
            delete_task(task_id)

    elif command == 'new_status':
        # Check if task ID and new status are provided
        if len(sys.argv) < 4:
            print("Use: task-cli new_status <ID> <new status>")
        else:
            task_id = int(sys.argv[2])
            new_status = sys.argv[3]
            status_task(task_id, new_status)

    else:
        print("Unknown command. Please use: add, list, update, delete, new_status")


if __name__ == "__main__":
    main()
