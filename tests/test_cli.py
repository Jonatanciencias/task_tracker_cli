import unittest
from unittest.mock import patch
import sys
from io import StringIO
from src.cli import main

class TestCLI(unittest.TestCase):

    @patch('sys.argv', ['task-cli'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_show_help(self, mock_stdout):
        main()
        self.assertIn("Task Tracker CLI:", mock_stdout.getvalue())

    @patch('sys.argv', ['task-cli', 'add'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_add_no_description(self, mock_stdout):
        main()
        self.assertIn("Use: task-cli add <description>", mock_stdout.getvalue())

    @patch('sys.argv', ['task-cli', 'add', 'Test task'])
    @patch('src.cli.add_task', return_value={'id': 1, 'description': 'Test task', 'status': 'pending'})
    @patch('sys.stdout', new_callable=StringIO)
    def test_add_task(self, mock_stdout, mock_add_task):
        main()
        self.assertIn("Tas added sucefully: 1", mock_stdout.getvalue())

    @patch('sys.argv', ['task-cli', 'list'])
    @patch('src.cli.load_tasks', return_value=[{'id': 1, 'description': 'Test task', 'status': 'pending'}])
    @patch('sys.stdout', new_callable=StringIO)
    def test_list_tasks(self, mock_stdout, mock_load_tasks):
        main()
        self.assertIn("ID: 1, Description: Test task, Status: pending", mock_stdout.getvalue())

    @patch('sys.argv', ['task-cli', 'list'])
    @patch('src.cli.load_tasks', return_value=[])
    @patch('sys.stdout', new_callable=StringIO)
    def test_list_no_tasks(self, mock_stdout, mock_load_tasks):
        main()
        self.assertIn("No tasks found", mock_stdout.getvalue())

    @patch('sys.argv', ['task-cli', 'update'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_update_no_id(self, mock_stdout):
        main()
        self.assertIn("Uso: task-cli update <ID> <nueva descripcion>", mock_stdout.getvalue())

    @patch('sys.argv', ['task-cli', 'update', '1', 'Updated task'])
    @patch('src.cli.update_task')
    def test_update_task(self, mock_update_task):
        main()
        mock_update_task.assert_called_with(1, 'Updated task')

    @patch('sys.argv', ['task-cli', 'delete'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_delete_no_id(self, mock_stdout):
        main()
        self.assertIn("Uso: task-cli delete <ID>", mock_stdout.getvalue())

    @patch('sys.argv', ['task-cli', 'delete', '1'])
    @patch('src.cli.delete_task')
    def test_delete_task(self, mock_delete_task):
        main()
        mock_delete_task.assert_called_with(1)

    @patch('sys.argv', ['task-cli', 'new_status'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_new_status_no_id(self, mock_stdout):
        main()
        self.assertIn("Uso: task-cli new_status <ID> <nuevo estado>", mock_stdout.getvalue())

    @patch('sys.argv', ['task-cli', 'new_status', '1', 'completed'])
    @patch('src.cli.status_task')
    def test_new_status_task(self, mock_status_task):
        main()
        mock_status_task.assert_called_with(1, 'completed')

    @patch('sys.argv', ['task-cli', 'unknown'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_unknown_command(self, mock_stdout):
        main()
        self.assertIn("Unknown comand, please use: add, list, update, delete, new_status", mock_stdout.getvalue())

if __name__ == '__main__':
    unittest.main()