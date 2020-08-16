import json

class Todo_Item:
    def __init__(self, is_done, name, due_date, number, class_name='misc', is_done_check='[ ]'):
        self.is_done = is_done
        self.name = name
        self.due_date = due_date
        self.number = number
        self.is_done_check = '[X]' if self.is_done else '[ ]'
        self.class_name = class_name if class_name is not None else 'none'

    def __str__(self):
        return f' {str(self.number)}. {self.is_done_check} {self.name}. Due: {self.due_date}. Class: {self.class_name}'

    def mark_as_completed(self):
        self.is_done_check = '[x]'
        self.is_done = True
        #! update json here

    def mark_as_incomplete(self):
        self.is_done_check = '[ ]'
        self.is_done = False
        #! update json here

    @classmethod
    def load_objects_from_json(cls): #makes json objects/dicts into python objects
        todo_list = []
        with open('todolist.json', 'r') as json_file:
            todo_items = json.loads(json_file.read())
            for i in todo_items:
                todo_list.append(cls(**i))
        json_file.close()
        return todo_list



        