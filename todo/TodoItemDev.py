import ujson as json
import dateparser
import os
from types import SimpleNamespace
from todo.MainTask import MainTask


# ┖╶╶╶>

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'secrets2.txt')
with open(my_file) as f:
    location = f.readline().strip('\n')


class TodoItem:
    def __init__(self, name, due_date, number, is_done_check='[ ]', class_name='none'):
        self.name = name
        self.due_date = due_date
        self.number = number
        self.is_done_check = is_done_check
        self.class_name = class_name if class_name is not None else 'none'

    def __str__(self):
        return f' {str(self.number)}. {self.is_done_check} {self.name.title()}\n   Due: {self.due_date.title()}, Class: {self.class_name.upper()}\n '

    def mark_as_completed(self):

        with open(location) as file:
            data = json.load(file)

        for item in data['todoitems']:
            if item['number'] == self.number:
                item["is_done_check"] = "[X]"

        with open(location, 'w') as json_file:
            json.dump(data, json_file, indent=4)

    def mark_as_incomplete(self):
        with open(location) as file:
            data = json.load(file)

        for item in data['todoitems']:
            if item['number'] == self.number:
                item["is_done_check"] = "[ ]"

        with open(location, 'w') as json_file:
            json.dump(data, json_file, indent=4)

    def edit(self, part, edited):
        with open(location) as file:
            data = json.load(file)

        if part.upper() == 'item'.upper():
            for item in data['todoitems']:
                if item['number'] == self.number:
                    item['name'] = edited

        elif part.upper() == 'date'.upper():
            if edited == 'td':
                edited = 'today'
            elif edited == 'tm':
                edited = 'tomorrow'
                
            for item in data['todoitems']:
                if item['number'] == self.number:
                    item['due_date'] = dateparser.parse(edited).strftime('%A %B %d %Y')

        elif part.upper() == 'class'.upper():
            for item in data['todoitems']:
                if item['number'] == self.number:
                    item['class_name'] = edited

        with open(location, 'w') as json_file:
            json.dump(data, json_file, indent=4)

    def add_to_json(self, item, file):

        with open(location) as json_file:
            data = json.load(json_file)
            temp = data['todoitems']
            item_dict = item.__dict__
            temp.append(item_dict)

        with open(location, 'w') as f:
            json.dump(data, f, indent=4)

    def remove_from_json(self, number):
        with open(location) as json_file:
            data = json.load(json_file)

        for item in data['todoitems']:
            if item['number'] == self.number:
                data['todoitems'].remove(item)
            if item['number'] > number:
                item['number'] = item['number'] - 1

        with open(location, 'w') as json_file:
            json.dump(data, json_file, indent=4)

    @classmethod
    def mark_all_complete(cls):
        with open(location) as json_file:
            data = json.load(json_file)

        for item in data['todoitems']:
            item['is_done_check'] = '[X]'

        with open(location, 'w') as json_file:
            json.dump(data, json_file, indent=4)

    @classmethod
    def remove_all_completed(cls):
        # Load the data from the JSON file
        with open(location, 'r') as json_file:
            data = json.load(json_file)

        # Filter out items where 'is_done_check' is '[X]'
        data['todoitems'] = [item for item in data['todoitems'] if item['is_done_check'] != '[X]']

        # Update the numbering
        for i, item in enumerate(data['todoitems']):
            item['number'] = i + 1

        # Save the updated data back to the JSON file
        with open(location, 'w') as json_file:
            json.dump(data, json_file, indent=4)

    @staticmethod
    def load_objects_from_json(file):  # makes json objects/dicts into MainTask objects
        todo_list = []
        with open(file, 'r') as file:
            json_data = file.read()

        python_object = json.loads(json_data)
        
        todo_items = python_object.get('todoitems', [])

        for item in todo_items:
            todo_list.append(MainTask.dict_to_task(item))

        return todo_list
