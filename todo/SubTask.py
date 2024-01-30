from todo.Task import Task
import ujson as json
import os
import uuid

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'secrets2.txt')
with open(my_file) as f:
    location = f.readline().strip('\n')
class SubTask(Task):
    # TODO: Complete implementation of subtask

    def __init__(self, name, due_date, number, is_done_check='[ ]', id=str(uuid.uuid4())):
        self.id = id
        self.name = name
        self.due_date = due_date
        self.number = number
        self.is_done_check = is_done_check

    def __str__(self) -> str:
        return f' {str(self.number)}. {self.is_done_check} {self.name.title()}\n   Due: {self.due_date.title()}'
    
    def to_dict(self):
        return {
            'id': str(self.id),
            'name': self.name,
            'due_date': self.due_date,
            'number': self.number,
            'is_done_check': self.is_done_check
        }

    def add_sub_to_json(self, location, item_number):
        with open(location) as json_file:
            data = json.load(json_file)
            if item_number < 0 or item_number >= len(data['todoitems']):
                print("Invalid todo item number.")
                return
        
            data['todoitems'][item_number]['subtasks'].append(self.__dict__)

        with open(location, 'w') as f:
            json.dump(data, f, indent=4)
    
    @classmethod
    def dict_to_subtask(cls, subtask_dicts):
        # Using list comprehension for efficient conversion
        return [cls(**subtask_dict) for subtask_dict in subtask_dicts]
    
    def subtask_progress_bar(self):
        pass

    def mark_as_completed(self, item):
        self.is_done_check = '[X]'

        with open(location) as json_file:
            data = json.load(json_file)

        for task in data['todoitems']:
            if task['number'] == item:
                for sub in task['subtasks']:
                    if sub['number'] == self.number:
                        sub['is_done_check'] = '[X]'
        
        with open(location, 'w') as f:
            json.dump(data, f, indent=4)

    def mark_as_incomplete(self, item):
        self.is_done_check = '[ ]'

        with open(location) as json_file:
            data = json.load(json_file)

        for task in data['todoitems']:
            if task['number'] == item:
                for sub in task['subtasks']:
                    if sub['number'] == self.number:
                        sub['is_done_check'] = '[ ]'
        
        with open(location, 'w') as f:
            json.dump(data, f, indent=4)

    def edit_name(self, edited_name, item_number):
        self.name = edited_name

        with open(location) as json_file:
            data = json.load(json_file)

        for item in data['todoitems']:
            if item['number'] == item_number:
                for sub in item['subtasks']:
                    if sub['number'] == self.number:
                        sub['name'] = edited_name

        with open(location, 'w') as f:
            json.dump(data, f, indent=4)

    def edit_date(self, edited_date, item_number):
        self.due_date = edited_date

        with open(location) as json_file:
            data = json.load(json_file)

        for item in data['todoitems']:
            if item['number'] == item_number:
                for sub in item['subtasks']:
                    if sub['number'] == self.number:
                        sub['due_date'] = edited_date

        with open(location, 'w') as f:
            json.dump(data, f, indent=4)

    def remove_sub_from_json(self, item, sub):
        with open(location) as json_file:
            data = json.load(json_file)

        for task in data['todoitems']:
            if task['number'] == item:
                if sub == "done":
                    # Remove all subtasks that are marked as done
                    task['subtasks'] = [subtask for subtask in task['subtasks'] if subtask['is_done_check'] != '[X]']
                else:
                    # Remove a specific subtask by filtering
                    sub = int(sub)
                    task['subtasks'] = [subtask for subtask in task['subtasks'] if subtask['number'] != sub]

                # Adjust the numbering for remaining subtasks
                for i, subtask in enumerate(task['subtasks'], start=1):
                    subtask['number'] = i

        # Write the updated data back to the JSON file
        with open(location, 'w') as json_file:
            json.dump(data, json_file, indent=4)

    