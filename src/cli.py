# src/cli.py

import sys
from task_manager import load_tasks, add_task, update_task, delete_task, status_task

def show_help():
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

    The main function parses the command line arguments and executes the corresponding commands.
    It supports the following commands:
    - add: Adds a new task with the provided description.
    - list: Lists all the tasks with their IDs, descriptions, and statuses.
    - update: Updates the description of a task with the provided ID.
    - delete: Deletes a task with the provided ID.
    - new_status: Updates the status of a task with the provided ID.

    Usage:
    - add: task-cli add <description>
    - list: task-cli list
    - update: task-cli update <ID> <new description>
    - delete: task-cli delete <ID>
    - new_status: task-cli new_status <ID> <new status>

    Example:
    $ task-cli add "Finish documentation"
    Task added successfully: 123

    $ task-cli list
    ID: 123, Description: Finish documentation, Status: In Progress

    $ task-cli update 123 "Finish documentation and testing"
    Task updated successfully.

    $ task-cli delete 123
    Task deleted successfully.

    $ task-cli new_status 123 Done
    Task status updated successfully.
    """
    # Rest of the code...
    if len(sys.argv) < 2:
        show_help()
        return
    command = sys.argv[1]  
    if command == 'add':
        if len(sys.argv) < 3:
            print("Use: task-cli add <description> ")
        else:
            description = ' '.join(sys.argv[2:])
            task = add_task(description)
            print(f"Tas added sucefully: {task['id']}")
    elif command == 'list':
        tasks = load_tasks()
        if tasks:
            for task in tasks:
                print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}")
        else:
            print("No tasks found")
    elif command == 'update':
        if len(sys.argv) < 4:
            print("Uso: task-cli update <ID> <nueva descripcion>")
        else:
            task_id = int(sys.argv[2])
            new_description = " ".join(sys.argv[3:])
            update_task(task_id, new_description)
    elif command == 'delete':
        if len(sys.argv) < 3:
            print("Uso: task-cli delete <ID>")
        else:
            task_id = int(sys.argv[2])
            delete_task(task_id)
    elif command == 'new_status':
        if len(sys.argv) < 4:
            print("Uso: task-cli new_status <ID> <nuevo estado>")
        else:
            task_id = int(sys.argv[2])
            new_status = sys.argv[3]
            status_task(task_id, new_status)
    else:
        print("Unknown comand, please use: add, list, update, delete, new_status")          

if __name__ == "__main__":
    main()  