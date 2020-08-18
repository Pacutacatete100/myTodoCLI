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

        

    # def remove_from_json(self):
    #     #! update json here


    @classmethod
    def load_objects_from_json(cls): #makes json objects/dicts into python objects
        todo_list = []
        with open('todolist.json', 'r') as json_file:
            todo_items = json.loads(json_file.read())
            for i in todo_items['todoitems']:
                todo_list.append(cls(**i))
        json_file.close()
        return todo_list



        