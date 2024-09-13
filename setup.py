"""Library configuration file."""
from setuptools import setup, find_packages

setup(
    name='task-tracker-cli',
    version='1.0.0',
    packages=find_packages(where="src"),  # Search for packages in the 'src' directory
    package_dir={"": "src"},  # Specify that the source code is in the 'src' folder
    install_requires=[],  # If you need to install any dependencies
    entry_points={
        'console_scripts': [
            'task-cli=cli.py:main',  # Specify that the 'task-cli' command will execute the 'main' function in 'cli.py'
        ],
    },
)
