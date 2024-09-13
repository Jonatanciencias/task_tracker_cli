"""Command-line interface for Task Tracker CLI application."""

import sys
import os
from task_manager import load_tasks, add_task, update_task, delete_task, status_task

def show_help():
    """
    Displays the help message for Task Tracker CLI, outlining the available commands and their usage.
    """
    help_message = """
    Task Tracker CLI:

    Comandos:
    - add <descripcion>: Añade una nueva tarea con la descripción proporcionada.
    - list: Lista todas las tareas.
    - update <ID> <descripcion>: Actualiza la tarea con el ID especificado y la nueva descripción.
    - delete <ID>: Elimina la tarea con el ID especificado.
    - new_status <ID> <status>: Cambia el estado de la tarea con el ID proporcionado.

    Ejemplos:
    - task-cli add "Finalizar documentación"
    - task-cli list
    - task-cli update 123 "Actualizar la descripción de la tarea"
    - task-cli delete 123
    - task-cli new_status 123 done
    """
    print(help_message)

def main():
    """
    Entry point for the Task Tracker CLI application.
    Parses command-line arguments and executes corresponding commands.
    """
    if len(sys.argv) < 2:
        show_help()
        return

    command = sys.argv[1]

    # Maneja los diferentes comandos
    if command == 'add':
        if len(sys.argv) < 3:
            print("Uso: task-cli add <descripcion>")
        else:
            description = ' '.join(sys.argv[2:])
            task = add_task(description)
            print(f"Tarea añadida exitosamente: {task['id']}")

    elif command == 'list':
        tasks = load_tasks()
        if tasks:
            for task in tasks:
                print(f"ID: {task['id']}, Descripción: {task['description']}, Estado: {task['status']}")
        else:
            print("No se encontraron tareas.")

    elif command == 'update':
        if len(sys.argv) < 4:
            print("Uso: task-cli update <ID> <nueva descripción>")
        else:
            task_id = int(sys.argv[2])
            new_description = ' '.join(sys.argv[3:])
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
        print("Comando desconocido. Los comandos disponibles son: add, list, update, delete, new_status.")

if __name__ == "__main__":
    main()
