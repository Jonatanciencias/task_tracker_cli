import unittest
from io import StringIO
from unittest.mock import patch
from src.cli import main
from src.task_manager import load_tasks, save_tasks
import os

class TestCLI(unittest.TestCase):
    """
    A test case class for testing the CLI functionality.
    Methods:
    - setUp: Prepares a temporary tasks file for testing.
    - tearDown: Removes the test file after each test.
    - test_add_task_cli: Test the add command in the CLI.
    """

    def setUp(self):
        """
        Set up the test environment for the test_cli module.
        This method is executed before each test case in the module.
        Parameters:
        - None
        Returns:
        - None
        """
        self.test_tasks_file = 'test_tasks.json'
        global TASKS_FILE
        TASKS_FILE = self.test_tasks_file
        save_tasks([])  # Start with an empty tasks file

    def tearDown(self):
        """
        Clean up method that is called after each test case.
        Removes the test tasks file if it exists.
        """
        if os.path.exists(self.test_tasks_file):
            os.remove(self.test_tasks_file)

    @patch('sys.stdout', new_callable=StringIO)
    @patch('sys.argv', ['cli.py', 'add', 'Test task'])   
    def test_add_task_cli(self, mock_stdout):
        """
        Test case for the `add_task_cli` function.
        This test case verifies that the `add_task_cli` function adds a task successfully and updates the task list accordingly.
        Parameters:
            mock_stdout (Mock): A mock object representing the standard output.
        Assertions:
            - Verifies that the output of the function contains the message "Task added successfully".
            - Verifies that the length of the task list is 1 after calling the function.
        Returns:
            None
        """
        main()  # Call the main CLI function
        output = mock_stdout.getvalue().strip()
        self.assertIn("Task added successfully", output)
        
        tasks = load_tasks()
        self.assertEqual(len(tasks), 1)
  
