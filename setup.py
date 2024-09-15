""" This file is used to define the package and its dependencies. It also defines the command that will be used to run the CLI. """
from setuptools import setup, find_packages

setup(
    name='task-tracker-cli',
    version='2.0.0',
    packages=find_packages(),
    install_requires=[
        # Add any dependencies your project needs here
    ],
    entry_points={
        'console_scripts': [
            'task-cli=src.cli:main',  # This defines 'task-cli' as the command to run the 'main' function from 'cli.py'.
        ],
    },
)
