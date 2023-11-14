from setuptools import setup

setup(
    name='{{cookiecutter.project_name}}',
    version='0.1',
    packages=['{{cookiecutter.project_name}}'],
    entry_points={
        'console_scripts': ['{{cookiecutter.project_name}} = {{cookiecutter.directory_name}}.{{cookiecutter.file_name}}:main'],
    },
)
