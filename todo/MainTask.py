from todo.Task import Task
from todo.SubTask import SubTask
import ujson as json

class MainTask(Task):
    
    def __init__(self, name, due_date, number, classname, is_done_check='[ ]', subtasks=[]):
        self.name = name
        self.due_date = due_date
        self.number = number
        self.classname = classname
        self.is_done_check = is_done_check
        self.subtasks = subtasks

    def __str__(self) -> str:
        if len(self.subtasks )<=0:
            return f' {str(self.number)}. {self.is_done_check} {self.name.title()}\n   Due: {self.due_date.title()}, Class: {self.classname.upper()}\n '
        else:
            return f' {str(self.number)}. {self.is_done_check} {self.name.title()}\n   Due: {self.due_date.title()}, Class: {self.classname.upper()}\n    ┖╶╶╶> {len(self.subtasks)} subtasks\n'
        
    @staticmethod
    def dict_to_task(task_dict):
        return MainTask(
            name=task_dict['name'],
            due_date=task_dict['due_date'],
            number=task_dict['number'],
            classname=task_dict['classname'],
            is_done_check=task_dict['is_done_check'],
            subtasks=SubTask.dict_to_subtask(task_dict['subtasks'])
        )
    
    def to_dict(self):
        # Convert MainTask and its SubTasks to a dictionary
        return {
            'name': self.name,
            'due_date': self.due_date,
            'number': self.number,
            'classname': self.classname,
            'is_done_check': self.is_done_check,
            'subtasks': [subtask.to_dict() for subtask in self.subtasks]
        }

    def add_to_json(self, location):
        with open(location) as json_file:
            data = json.load(json_file)
            temp = data['todoitems']
            item_dict = self.__dict__
            temp.append(item_dict)

        with open(location, 'w') as f:
            json.dump(data, f, indent=4)

    def print_subtasks(self):
        for s in self.subtasks:
            print(s)

    def mark_as_completed(self):
        pass

    def mark_as_incomplete(self):
        pass

    def edit_name(self, edited_name):
        pass

    def edit_date(self, edited_date):
        pass

    def edit_classname(self, edited_classname):
        pass

    def remove_from_json(self):
        pass

    def add_subtask(self, subtask, item_number, location):
        pass
