import json
import os
import unittest

from src.task_manager import (add_task, delete_task, load_tasks, save_tasks,
                              status_task, update_task)


class TestTaskManager(unittest.TestCase):
    """
    A test case for the TaskManager class.
    Methods:
    - setUp(): Prepares a temporary tasks file for testing.
    - tearDown(): Removes the test file after each test.
    - test_add_task(): Tests that a new task is added correctly.
    - test_delete_task(): Tests that a task is deleted correctly.
    - test_update_task(): Tests that a task is updated correctly.
    - test_status_task(): Tests that the status of a task is changed correctly.
    """

    def setUp(self):
        """
        Set up method that is executed before each test case.

        It initializes the test_tasks_file variable with the value 'test_tasks.json'.
        It sets the global TASKS_FILE variable to the value of test_tasks_file.
        It saves an empty list of tasks to the tasks file using the save_tasks function.
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

    def test_add_task(self):
        """
        Test case for the add_task function.
        This test case verifies that the add_task function correctly adds a task to the task manager.
        It checks that the task is added with the correct description and status.
        Steps:
        1. Call the add_task function with a test task description.
        2. Load the tasks from the task manager.
        3. Assert that the number of tasks is 1.
        4. Assert that the description of the first task is equal to the test task description.
        5. Assert that the status of the first task is 'to-do'.
        """
        task = add_task("Test task")
        tasks = load_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]['description'], "Test task")
        self.assertEqual(tasks[0]['status'], 'to-do')

    def test_delete_task(self):
        """
        Test case for deleting a task.
        This test case verifies that a task is successfully deleted from the task manager.
        Steps:
        1. Add a task to the task manager.
        2. Load the tasks from the task manager.
        3. Delete the first task from the loaded tasks.
        4. Load the tasks again.
        5. Assert that the number of tasks is 0.
        """

        add_task("Task to delete")
        tasks = load_tasks()
        delete_task(tasks[0]['id'])
        tasks = load_tasks()
        self.assertEqual(len(tasks), 0)

    def test_update_task(self):
        """
        Test case for the update_task function.
        This test case verifies that the update_task function correctly updates the description of a task.
        Steps:
        1. Add a task with the description "Old task".
        2. Call the update_task function with the task ID and the new description "Updated task".
        3. Load the tasks.
        4. Assert that the description of the first task in the list is equal to "Updated task".
        """
        add_task("Old task")
        update_task(1, "Updated task")
        tasks = load_tasks()
        self.assertEqual(tasks[0]['description'], "Updated task")

    def test_status_task(self):
        """
        Test case for the status_task function.
        This test case verifies that the status of a task is correctly updated when the status_task function is called.
        Steps:
        1. Add a task with the description "Task to change status".
        2. Call the status_task function with the task ID and the new status "done".
        3. Load the tasks from the task manager.
        4. Assert that the status of the first task in the list is "done".
        """
        add_task("Task to change status")
        status_task(1, "done")
        tasks = load_tasks()
        self.assertEqual(tasks[0]['status'], "done")

    def test_update_non_existent_task(self):
        """
        Test case for updating a non-existent task.
        This test case verifies that when attempting to update a task that does not exist,
        the update_task function returns None and the number of tasks remains unchanged.
        Steps:
        1. Call the update_task function with a non-existent task ID and a new task description.
        2. Load the tasks from the task manager.
        3. Assert that the number of tasks is still 0.
        4. Assert that the result of the update_task function is None.
        Expected behavior:
        - The update_task function should return None.
        - The number of tasks should remain unchanged.
        """
        result = update_task(999, "Non-existent task update")
        tasks = load_tasks()
        self.assertEqual(len(tasks), 0)
        self.assertIsNone(result, "Attempting to update a non-existent task should return None "
                      "or a proper error message.")
