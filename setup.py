""" Configuration file for packaging the project into a Python package """

import os
from setuptools import setup, find_packages

# Load the contents of the README.md file for the long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='task-tracker-cli',
    version='1.0.0',
    author="Jonatan Garcia",
    author_email="jonatanciencias@gmail.com",
    description="A CLI for managing tasks from the terminal",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Jonatanciencias/task_tracker_cli",
    project_urls={
        "Bug Tracker": "https://github.com/Jonatanciencias/task_tracker_cli/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(where='src'),  # Find and list packages in 'src'
    package_dir={'': 'src'},  # Base directory where packages are located
    python_requires='>=3.6',  # Specify the minimum Python version
    install_requires=[],  # Specify package dependencies here
    extras_require={  # Optional dependencies for development
        'dev': [
            'pytest>=6.0',  # For running unit tests
        ],
    },
    entry_points={  # Entry point for command line
        'console_scripts': [
            'task-cli = src/cli:main',  # The CLI command to be installed
        ],
    },
    include_package_data=True,  # Include additional files specified in MANIFEST.in
)
