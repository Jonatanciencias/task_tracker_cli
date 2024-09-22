
---

# Task Tracker CLI

[home](src/screenshot_help.png)

A simple yet efficient task tracker that allows you to manage your tasks from the command line. **Task Tracker CLI** helps you organize and keep track of your daily tasks, allowing you to add, update, delete, and change task statuses directly from the terminal.

## Features

- **Add Tasks**: Add a task with a given description.
- **List Tasks**: Display all tasks with their ID, description, and status.
- **Update Tasks**: Update the description of an existing task.
- **Delete Tasks**: Delete a task by its ID.
- **Change Task Status**: Change the status of a task to "to-do", "in-progress", or "done".

## Requirements

- Python 3.6 or higher.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Jonatanciencias/task_tracker_cli.git
```

2. Navigate to the directory:

```bash
cd task_tracker_cli
```

3. Set up a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

4. Install the project using setup.py:
```bash
pip install .
```

4. Run help

```bash
task-cli help
```

## Usage

### Commands:

1. **Add Task**:

```bash
task-cli add "Task description"

```

2. **List Tasks**:

```bash
task-cli list

```
3. List Tasks by Status:  

```bash
task-cli list done
task-cli list todo
task-cli list in-progress

```

4. **Update Task**:

```bash
task-cli update <ID> "New description"

```

5. **Delete Task**:

```bash
task-cli delete <ID>
```

6. **Change Status**:

```bash
task-cli new_status <ID> <status>
```

7. **Uninstal**:
```bash
pip uninstall task-tracker-cli
```

## Testing

Unit tests are included to ensure the core functions work correctly. To run the tests:

```bash
python -m unittest discover tests
```

### Important Notice:

If you encounter no output or an error in the console while using the Task Tracker CLI, you can find detailed logs for troubleshooting.

1. *Log Location*: Logs are automatically saved in the following directory within your virtual environment:

```bash
\venv\Lib\site-packages\logs
```

2. *Checking Logs*: If the CLI does not behave as expected or an error occurs, check the utils.log file inside the logs folder for detailed information

## Original Project

This project is an implementation of the **Task Tracker CLI**, based on the projects proposed by **[roadmap.sh](https://roadmap.sh/projects/task-tracker)**.

## Contributions

Contributions are welcome! Please open an issue or submit a pull request.

---

### Repositorio GitHub:

**[https://github.com/Jonatanciencias/task_tracker_cli](https://github.com/Jonatanciencias/task_tracker_cli)**
