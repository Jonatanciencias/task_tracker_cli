"""This file is used to define the package and its dependencies. It also defines the command that will be used to run the CLI."""
from setuptools import setup, find_packages

setup(
    name='task-tracker-cli',
    version='2.0.0',
    packages=find_packages(),
    include_package_data=True,  # This ensures that non-code files like tasks.json and logs are included.
    install_requires=[
        # Add any dependencies your project needs here
        # For example: 'requests', 'click', etc.
    ],
    entry_points={
        'console_scripts': [
            'task-cli=src.cli:main',  # This defines 'task-cli' as the command to run the 'main' function from 'cli.py'.
        ],
    },
    package_data={
        '': ['*.json'],  # Include any .json files in the package (such as tasks.json).
    },
    data_files=[
        ('logs', []),  # Ensure the logs directory is created.
    ],
)
