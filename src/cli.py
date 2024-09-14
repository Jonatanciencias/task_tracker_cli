"""" Command Line Interface (CLI) for the Task Tracker application. """
import sys
import logging
import os

# Add the src directory to the system path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

try:
    from src.task_manager import load_tasks, add_task, update_task, delete_task, status_task

except ImportError:
    print("Unable to import 'task_manager'. Please ensure that the module is in the correct directory.")
    sys.exit(1)

# configure logging
logging.basicConfig(filename='task_cli.log', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug('start cli.py')


def show_help():
    """
    Displays the available commands in the CLI.
    """
    help_message = """
    Task Tracker CLI:
    
    Commands:
    - add <description>: Add a new task.
    - list: List all tasks.
    - update <ID> <description>: Update the task with the specified ID.
    - delete <ID>: Delete the task with the specified ID.
    - new_status <ID> <status>: Change the status of the task.
    """
    print(help_message)


def main():
    """
    Entry point of the task tracker CLI application.
    Parses command line arguments and executes corresponding commands.
    Usage:
        task-cli add <description> - Add a new task with the given description.
        task-cli list - List all tasks.
        task-cli update <ID> <new description> - Update the description of a task with the given ID.
        task-cli delete <ID> - Delete a task with the given ID.
        task-cli new_status <ID> <new status> - Update the status of a task with the given ID.
    Returns:
        None
    """
    logging.debug('Start of main() function')
    if len(sys.argv) < 2:
        logging.debug('Not enough arguments provided')
        show_help()
        return
    command = sys.argv[1]
    logging.debug('Received command: %s', command)
    if command == 'add':
        if len(sys.argv) < 3:
            logging.error("Task description is missing")
            print("Usage: task-cli add <description>")
        else:
            description = ' '.join(sys.argv[2:])
            task = add_task(description)
            logging.info('Task added: %s', task)
            print(f"Task added successfully: ID {task['id']}")

    elif command == 'list':
        tasks = load_tasks(file_path='tasks.json')
        if tasks:
            for task in tasks:
                print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}")
        else:
            print("No tasks found.")

    elif command == 'update':
        if len(sys.argv) < 4:
            print("Usage: task-cli update <ID> <new description>")
        else:
            task_id = int(sys.argv[2])
            new_description = ' '.join(sys.argv[3:])
            update_task(task_id, new_description)
            print(f"Task {task_id} updated successfully.")

    elif command == 'delete':
        if len(sys.argv) < 3:
            print("Usage: task-cli delete <ID>")
        else:
            task_id = int(sys.argv[2])
            delete_task(task_id)
            print(f"Task {task_id} deleted successfully.")

    elif command == 'new_status':
        if len(sys.argv) < 4:
            print("Usage: task-cli new_status <ID> <new status>")
        else:
            task_id = int(sys.argv[2])
            new_status = sys.argv[3]
            status_task(task_id, new_status)
            print(f"Status of task {task_id} updated to '{new_status}'.")

    else:
        print("Unknown command. Available commands: add, list, update, delete, new_status")
        show_help()


if __name__ == "__main__":
    main()
