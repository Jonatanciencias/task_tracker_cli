"""This file is necessary for the package to be installed with pip."""
from setuptools import setup, find_packages

setup(
    name='task-tracker-cli',
    version='1.0.0',
    packages=find_packages(include=['src', 'src.*']),
    entry_points={
        'console_scripts': [
            'task-cli = src.cli:main', 
        ],
    },
)
