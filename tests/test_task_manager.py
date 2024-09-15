"""Unit tests for the task_manager module."""

import unittest
import os
import logging
from src.task_manager import add_task, update_task, delete_task, load_tasks, new_status_task

# Configure logging for the test suite
logging.basicConfig(filename='test_task_manager.log', level=logging.DEBUG, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

class TestTaskManager(unittest.TestCase):
    """
    A test case class for testing the TaskManager functions.
    Methods:
    - setUp: Initializes the test tasks file.
    - test_add_task: Tests task addition.
    - test_update_task: Tests task update.
    - test_delete_task: Tests task deletion.
    - test_status_task: Tests task status change.
    - tearDown: Cleans up the test environment.
    """
    
    def setUp(self):
        """Initializes the test tasks file with an empty list."""
        logging.debug('Setting up the test environment.')
        self.tasks_file = 'test_tasks_manager.json'  # Use a clear and specific name for the test file
        with open(self.tasks_file, 'w', encoding='utf-8') as file:
            file.write('[]')
        logging.info("Test file %s created.", self.tasks_file)

    def test_add_task(self):
        """Tests that tasks are correctly added to the task manager."""
        logging.debug('Testing task addition.')
        add_task("New task", file_path=self.tasks_file)
        tasks = load_tasks(file_path=self.tasks_file)
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]['description'], "New task")
        logging.info('Task added successfully.')

    def test_update_task(self):
        """Tests that task descriptions are correctly updated."""
        logging.debug('Testing task update.')
        add_task("Task to update", file_path=self.tasks_file)
        update_task(1, "Updated task", file_path=self.tasks_file)
        tasks = load_tasks(file_path=self.tasks_file)
        self.assertEqual(tasks[0]['description'], "Updated task")
        logging.info('Task updated successfully.')

    def test_delete_task(self):
        """Tests that tasks are correctly deleted."""
        logging.debug('Testing task deletion.')
        add_task("Task to delete", file_path=self.tasks_file)
        delete_task(1, file_path=self.tasks_file)
        tasks = load_tasks(file_path=self.tasks_file)
        self.assertEqual(len(tasks), 0)
        logging.info('Task deleted successfully.')

    def test_status_task(self):
        """Tests that task statuses are correctly updated."""
        logging.debug('Testing task status change.')
        add_task("Task to change status", file_path=self.tasks_file)
        new_status_task(1, "done", file_path=self.tasks_file)
        tasks = load_tasks(file_path=self.tasks_file)
        self.assertEqual(tasks[0]['status'], "done")
        logging.info('Task status updated successfully.')

    def tearDown(self):
        """Cleans up the test tasks file after each test."""
        logging.debug('Tearing down the test environment.')
        if os.path.exists(self.tasks_file):
            os.remove(self.tasks_file)
            logging.info(f"Test file {self.tasks_file} removed.")

if __name__ == '__main__':
    unittest.main()
