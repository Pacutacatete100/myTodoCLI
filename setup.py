from setuptools import setup
setup(
    name = 'MyTodoCLI',
    version = '0.1.0',
    packages = ['todo'],
    entry_points = {
        'console_scripts': [
            'todo = todo.__main__:main'
        ]
    })
