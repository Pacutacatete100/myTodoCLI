import json
import click
from todo.MainTask import MainTask
from todo.SubTask import SubTask

'''TODO:
    - load objects from json
    - progress bar for main tasks and for all subtasks
    - modification functions for json should go here
        - adding
        - removing
        - marking main tasks as complete/incomplete
        - marking subtasks as complete/incomplete
        - editing'''

class TodoList():
    def __init__(self, location):
        self.data = self.load_objects_from_json(location)

    def load_objects_from_json(self, file):  # makes json objects/dicts into MainTask objects
        todo_list = []
        with open(file, 'r') as file:
            json_data = file.read()

        python_object = json.loads(json_data)
        
        todo_items = python_object.get('todoitems', [])

        for item in todo_items:
            todo_list.append(MainTask.dict_to_task(item))

        return todo_list
    
    def main_progress_bar(self):
        list_len = len(self.data)
        num_items_done = 0

        bar_fixed_width = 42

        if list_len != 0:
            bar_increment_value = round(bar_fixed_width / list_len)

            for i in self.data:
                if i.is_done_check == '[X]':
                    num_items_done += 1
        
            progress_percent = round((num_items_done / list_len) * 100)

            progress_bar = ' ' * bar_fixed_width

            updated_progress_bar = progress_bar.replace(' ', '■', bar_increment_value*num_items_done)

            click.echo(click.style(f'|{updated_progress_bar}| {progress_percent}%', fg='green'))

        else:
            click.echo('No Items In List')

    def subtask_progress_bar(self):

        pass
        
    