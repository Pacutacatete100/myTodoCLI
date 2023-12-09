import json
import orjson
import click
import os
from todo.MainTask import MainTask
from todo.SubTask import SubTask

'''TODO:
    - create add function
        - should take in MainTask object
        - should also add that item to JSON here so that only TaskController.add() is called in CLI command definitino'''

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'secrets2.txt')
with open(my_file) as f:
    location = f.readline().strip('\n')
class TodoList:
    def __init__(self):
        self.data = self.load_objects_from_json()

    def __getitem__(self, index):
        return self.data[index]

    def __len__(self):
        return len(self.data)

    def __iter__(self):
        return iter(self.data)
    
    def load_objects_from_json(self):  # makes json objects/dicts into MainTask objects
        todo_list = []
        with open(location, 'r') as file:
            json_data = file.read()

        python_object = json.loads(json_data)
        
        todo_items = python_object.get('todoitems', [])

        for item in todo_items:
            todo_list.append(MainTask.dict_to_task(item))

        return todo_list
    
    def update_json(self, number, property, new_value):
        with open(location, 'rb') as file:
            data = orjson.loads(file.read())

        for task in data['todoitems']:
            if task['number'] == number:
                if property in task:
                    task[property] = new_value
                else:
                    print(f"Property '{property}' not found in the task.")
                break

        with open(location, 'wb') as file:
            file.write(orjson.dumps(data, option=orjson.OPT_INDENT_2))
    
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

    def add(self, main_task, location):
        self.data.append(main_task)
        main_task.add_to_json(location)

    def done(self, number):
        if number == 'all':
            for i in self.data:
                self.update_json(i+1, 'is_done_check','[X]')
        else:
            self.update_json(number, 'is_done_check','[X]')

    def undone(self, number):
        self.update_json(number, 'is_done_check','[ ]')

    def edit(self, number, update):
        pass

    def remove(self, number):
        pass
