from setuptools import setup
setup(
    name = 'MyTodoCLI',
    version = '0.1.0',
    py_modules = ['todo'],
    entry_points = {
        'console_scripts': [
            'todo = todo.todo:main',
            'tododev = todo.tododev:main'
        ]
    })
