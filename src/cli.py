""" Command Line Interface (CLI) for the Task Tracker application. """
import sys
from src.task_manager import load_tasks, add_task, update_task, delete_task, status_task


def show_help():
    help_message = """
    Task Tracker CLI:
    
    Comandos:
    - add <description>: Añade una nueva tarea.
    - list: Lista todas las tareas.
    - update <ID> <description>: Actualiza la tarea con el ID especificado.
    - delete <ID>: Elimina la tarea con el ID especificado.
    - new_status <ID> <status>: Cambia el estado de la tarea.
    """
    print(help_message)

def main():
    """
    Entry point of the Task Tracker CLI application.
    Usage:
        task-cli add <description> - Add a new task with the given description.
        task-cli list - List all tasks.
        task-cli update <ID> <new description> - Update the description of a task with the given ID.
        task-cli delete <ID> - Delete a task with the given ID.
        task-cli new_status <ID> <new status> - Update the status of a task with the given ID.
    """
    # Rest of the code...
    if len(sys.argv) < 2:
        show_help()
        return

    command = sys.argv[1]
    if command == 'add':
        if len(sys.argv) < 3:
            print("Uso: task-cli add <description>")
        else:
            description = ' '.join(sys.argv[2:])
            task = add_task(description)
            print(f"Task added successfully: {task['id']}")
    elif command == 'list':
        tasks = load_tasks()
        if tasks:
            for task in tasks:
                print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}")
        else:
            print("No tasks found")
    elif command == 'update':
        if len(sys.argv) < 4:
            print("Uso: task-cli update <ID> <new description>")
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
            print("Uso: task-cli new_status <ID> <new status>")
        else:
            task_id = int(sys.argv[2])
            new_status = sys.argv[3]
            status_task(task_id, new_status)
    else:
        print("Comando desconocido. Comandos disponibles: add, list, update, delete, new_status")

if __name__ == "__main__":
    main()
