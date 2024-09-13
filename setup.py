"""This file is necessary for the package to be installed with pip."""
from setuptools import setup, find_packages

from setuptools import setup, find_packages

setup(
    name="task-tracker-cli",
    version="1.0.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],
    entry_points={
        'console_scripts': [
            'task-cli=cli:main',
        ],
    },
)