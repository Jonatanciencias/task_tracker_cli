"""This file is necessary for the package to be installed with pip."""
from setuptools import setup, find_packages

setup(
    name="task-tracker-cli",
    version="1.0.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},  # Indica que los módulos están en la carpeta `src`
    install_requires=[],  # Si tienes dependencias, agrégalas aquí
    entry_points={
        'console_scripts': [
            'task-cli=src.cli:main',  # Asegúrate de que el punto de entrada esté correctamente configurado
        ],
    },
)
