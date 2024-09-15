#!/usr/bin/env python

""" Command Line Interface (CLI) for the Task Tracker application. """

import sys
import logging
import os

# Add the src directory to the system path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

try:
    from src.task_manager import load_tasks, add_task, update_task, delete_task, status_task
    from src.utils import show_help, validate_status
except ImportError as e:
    print(f"Import error: {e}")
    sys.exit(1)

# Set up logging configuration to log to file in the 'logs' directory
LOG_DIR = os.path.join(os.path.dirname(__file__), '..', 'logs')
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

log_file = os.path.join(LOG_DIR, 'task_cli.log')
logging.basicConfig(
    filename=log_file,
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode='w'  # Use 'a' for appending logs
)
logging.debug('CLI started.')

VALID_STATUSES = ['to-do', 'in-progress', 'done']


def main():
    """
    Entry point of the task tracker CLI application.
    Parses the command line arguments and executes the corresponding command.
    """
    logging.debug('Start of main() function')

    if len(sys.argv) < 2 or sys.argv[1] == 'help':
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
        if len(sys.argv) == 3:
            status_filter = sys.argv[2]
            
            # Validate the status
            if not validate_status(status_filter):
                return

            tasks = load_tasks(file_path='tasks.json')
            logging.debug("Loaded tasks: %s", tasks)
            filtered_tasks = [task for task in tasks if task['status'] == status_filter]

            if filtered_tasks:
                for task in filtered_tasks:
                    print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}")
            else:
                print(f"No tasks found with status '{status_filter}'.")

        else:
            tasks = load_tasks(file_path='tasks.json')
            logging.debug("Loaded tasks: %s", tasks)

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
            logging.info('Task %s updated', task_id)
            print(f"Task {task_id} updated successfully.")

    elif command == 'delete':
        if len(sys.argv) < 3:
            print("Usage: task-cli delete <ID>")
        else:
            task_id = int(sys.argv[2])
            delete_task(task_id)
            logging.info('Task %s deleted', task_id)
            print(f"Task {task_id} deleted successfully.")

    elif command == 'new_status':
        if len(sys.argv) < 4:
            print("Usage: task-cli new_status <ID> <new status>")
        else:
            task_id = int(sys.argv[2])
            new_status = sys.argv[3]
            
            if not validate_status(new_status):
                print(f"Error: '{new_status}' is not a valid status.")
            else:
                status_task(task_id, new_status)
                logging.info('Status of task %s updated to %s', task_id, new_status)
                print(f"Status of task {task_id} updated to '{new_status}'.")

    else:
        print("Unknown command. Available commands: add, list, update, delete, new_status")
        show_help()


if __name__ == "__main__":
    main()
