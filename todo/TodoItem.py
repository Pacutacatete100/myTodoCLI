import json

class Todo_Item:
    def __init__(self, name, due_date, number, is_done_check='[ ]', class_name='none' ):
        self.name = name
        self.due_date = due_date
        self.number = number
        self.is_done_check = is_done_check
        self.class_name = class_name if class_name is not None else 'none'

    def __str__(self):
        return f' {str(self.number)}. {self.is_done_check} {self.name.capitalize()}\n   Due: {self.due_date.capitalize()}, Class: {self.class_name.upper()}'

    def mark_as_completed(self):

        with open('todolist.json') as file:
            data = json.load(file)

        for item in data['todoitems']:
            if item['number'] == self.number:
                item["is_done_check"] = "[X]"

        with open('todolist.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)

    def mark_as_incomplete(self):
        with open('todolist.json') as file:
            data = json.load(file)

        for item in data['todoitems']:
            if item['number'] == self.number:
                item["is_done_check"] = "[ ]"

        with open('todolist.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)

    def add_to_json(self, item, file):
        def write_json(data, file_name='todolist.json'):
            with open(file_name, 'w') as f:
                json.dump(data, f, indent=4)
        with open('todolist.json') as json_file:
            data = json.load(json_file)
            temp = data['todoitems']
            item_dict = item.__dict__
            temp.append(item_dict)
        write_json(data)


    def remove_from_json(self, number):
        with open('todolist.json') as json_file:
            data = json.load(json_file)

        for item in data['todoitems'][:]:
            if item['number'] == self.number:
                data['todoitems'].remove(item)

        with open('todolist.json', 'w') as json_file:
            data = json.dump(data, json_file, indent=4)
        #! adjust numbers when removed


    @classmethod
    def load_objects_from_json(cls): #makes json objects/dicts into python objects
        todo_list = []
        with open('todolist.json', 'r') as json_file:
            todo_items = json.loads(json_file.read())
            for i in todo_items['todoitems']:
                todo_list.append(cls(**i))

        return todo_list


