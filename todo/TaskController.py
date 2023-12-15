import json
import orjson
import click
import os

from todo.MainTask import MainTask
from todo.SubTask import SubTask
from todo.DateProcessor import DateProcessor

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
    
    def load_objects_from_json(self):
        with open(location, 'rb') as file:
            # Read and parse JSON data in one go
            json_data = orjson.loads(file.read())

        # Directly create MainTask objects from the parsed data
        return [MainTask.dict_to_task(item) for item in json_data.get('todoitems', [])]
    
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

    def add(self, main_task):
        self.data.append(main_task)
        main_task.add_to_json(location)
        #TODO remove need for add_to_json

    def add_sub(self, subtask, number):
        self.data[number].add_subtask(subtask)
        subtask.add_sub_to_json(location, number)
        #TODO remove need for add_sub_to_json

    def done(self, number):
        if number == 'all':
            for i in self.data:
                i.mark_as_completed()
        else:
            self.data[int(number)-1].mark_as_completed()

    def undone(self, number):
        if number == 'all':
            for i in self.data:
                i.mark_as_incomplete()
        else:
            self.data[int(number)-1].mark_as_incomplete()

    def sub_done(self, item, subtask):
        self.data[item-1].subtasks[subtask-1].mark_as_completed(item)

        if self.data[item-1].all_subtasks_complete():
            self.data[item-1].mark_as_completed()

    def sub_undone(self, item, subtask):
        self.data[item-1].subtasks[subtask-1].mark_as_incomplete(item)
        if self.data[item-1].is_done_check == '[X]':
            self.data[item-1].mark_as_incomplete()

    def edit(self, number, update_part, update):
        for i in self.data:
            if i.number == int(number):
                if update_part == 'item':
                    i.edit_name(update)
                elif update_part == 'date':
                    i.edit_date(DateProcessor.process_date(update))
                elif update_part == 'class':
                    i.edit_classname(update)
                else:  
                    click.echo('Invalid Update Part')

    def edit_sub(self, item, sub, update_part, update):
        pass

    def remove(self, number):
        if number == 'done':
            for i in self.data:
                if i.is_done_check == '[X]':
                    self.data.remove(i)
                    i.remove_from_json(i.number)
        else:
            item_to_remove = self.data[int(number)-1]
            self.data.remove(item_to_remove)
            item_to_remove.remove_from_json(number)

        
