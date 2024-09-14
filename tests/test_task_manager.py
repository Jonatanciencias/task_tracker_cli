"""Unit tests for the task_manager module."""
import unittest
import os
from src.task_manager import add_task, update_task, delete_task, load_tasks, status_task

class TestTaskManager(unittest.TestCase):
    """
    A test case class for testing the TaskManager class.
    Methods:
    - setUp: Prepares the tasks file with an empty list.
    - test_add_task: Tests the addition of tasks.
    - test_update_task: Tests the update of a task.
    - test_delete_task: Tests the deletion of a task.
    - test_status_task: Tests the change of status of a task.
    - tearDown: Removes the test tasks file.
    """

    def setUp(self):
        """Prepares the tasks file with an empty list."""
        self.tasks_file = 'tasks.json'
        with open(self.tasks_file, 'w', encoding='utf-8') as file:
            file.write('[]')
            
    def test_add_task(self):
        """Tests the addition of tasks."""
        add_task("New task")
        tasks = load_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]['description'], "New task")

    def test_update_task(self):
        """Tests the update of a task."""
        add_task("Task to update")
        update_task(1, "Updated task")
        tasks = load_tasks()
        self.assertEqual(tasks[0]['description'], "Updated task")

    def test_delete_task(self):
        """Tests the deletion of a task."""
        add_task("Task to delete")
        delete_task(1)
        tasks = load_tasks()
        self.assertEqual(len(tasks), 0)

    def test_status_task(self):
        """Tests the change of status of a task."""
        add_task("Task to change status")
        status_task(1, "done")
        tasks = load_tasks()
        self.assertEqual(tasks[0]['status'], "done")

    def tearDown(self):
        """Removes the test tasks file."""
        if os.path.exists(self.tasks_file):
            os.remove(self.tasks_file)

if __name__ == '__main__':
    unittest.main()
