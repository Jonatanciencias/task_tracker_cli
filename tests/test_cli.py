"""Tests for the CLI module."""
import unittest
from unittest.mock import patch
from io import StringIO
from src.cli import main

class TestCLI(unittest.TestCase):
    """
    Test adding a task from the CLI.
    """
    def setUp(self):
        """Clears the tasks file before each test."""
        with open('tasks.json', 'w', encoding='utf-8') as file:
            file.write('[]')

    @patch('sys.stdout', new_callable=StringIO)
    @patch('sys.argv', ['task-cli', 'add', 'Test task'])
    def test_add_task_cli(self, mock_stdout):
        """Test adding a task from the CLI."""
        main()
        self.assertIn('Task added successfully', mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    @patch('sys.argv', ['task-cli', 'list'])
    def test_list_tasks_cli(self, mock_stdout):
        """Test listing tasks from the CLI."""
        main()
        self.assertIn('No tasks found', mock_stdout.getvalue())

if __name__ == '__main__':
    unittest.main()
