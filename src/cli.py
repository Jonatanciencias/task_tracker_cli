#!/usr/bin/env python

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

def main():
    """
    Entry point of the task tracker CLI application.
    The main function parses the command line arguments and executes the corresponding command.
    Usage:
        task-cli add <description> - Add a new task with the provided description.
        task-cli list [status] - List all tasks or filter tasks by status.
        task-cli update <ID> <new description> - Update the description of a task with the provided ID.
        task-cli delete <ID> - Delete the task with the provided ID.
        task-cli new_status <ID> <new status> - Update the status of a task with the provided ID.
    Commands:
        add - Add a new task.
        list - List all tasks or filter tasks by status.
        update - Update the description of a task.
        delete - Delete a task.
        new_status - Update the status of a task.
    Arguments:
        <description> - The description of the task to be added.
        [status] - Optional. Filter tasks by status. Valid statuses are: to-do, in-progress, done.
        <ID> - The ID of the task to be updated or deleted.
        <new description> - The new description for the task.
        <new status> - The new status for the task.
    Examples:
        task-cli add "Implement login feature"
        task-cli list
        task-cli list in-progress
        task-cli update 1 "Fix bug in registration form"
        task-cli delete 2
        task-cli new_status 3 done
    """
    # code implementation

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
        if len(sys.argv) == 3:
            status_filter = sys.argv[2]
            valid_statuses = ['to-do', 'in-progress', 'done']
            if status_filter not in valid_statuses:
                print(f"Invalid status '{status_filter}'. Valid statuses are: {', '.join(valid_statuses)}.")
                return
            tasks = load_tasks(file_path='tasks.json')
            filtered_tasks = [task for task in tasks if task['status'] == status_filter]
            if filtered_tasks:
                for task in filtered_tasks:
                    print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}")
            else:
                print(f"No tasks found with status '{status_filter}'.")
        else:
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
