from todo.Task import Task
from todo.SubTask import SubTask
import ujson as json
import os

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'secrets2.txt')
with open(my_file) as f:
    location = f.readline().strip('\n')
class MainTask(Task):
    
    def __init__(self, name, due_date, number, classname, is_done_check='[ ]', subtasks=[]):
        self.name = name
        self.due_date = due_date
        self.number = number
        self.classname = classname
        self.is_done_check = is_done_check
        self.subtasks = subtasks

    def __str__(self):
        return f' {str(self.number)}. {self.is_done_check} {self.name.title()}\n   Due: {self.due_date.title()}, Class: {self.classname.upper()} '

    def str_with_bar(self) -> str:
        if len(self.subtasks )<=0:
            return f' {str(self.number)}. {self.is_done_check} {self.name.title()}\n   Due: {self.due_date.title()}, Class: {self.classname.upper()}\n    ┗━━🞂 No Subtasks'
        else:
            return f' {str(self.number)}. {self.is_done_check} {self.name.title()}\n   Due: {self.due_date.title()}, Class: {self.classname.upper()}\n    ┗━━🞂 {self.subtask_progress_bar()}  {self.number_of_subs_complete()}/{len(self.subtasks)}'
        
    def expanded_view(self) -> str:
        lines = [
            f" {self.number}. {self.is_done_check} {self.name.title()}",
            f"   Due: {self.due_date.title()}, Class: {self.classname.upper()}"
        ]
        lines.append('   ┃')
        for i, subtask in enumerate(self.subtasks):
            if i == len(self.subtasks) - 1:  # Check if it's the last subtask
                prefix = "┗━"
                lines.append(f"   {prefix} {subtask.number}. {subtask.is_done_check} {subtask.name.title()}")
                lines.append(f"        Due: {subtask.due_date}")  # No vertical line for the last subtask
            else:
                prefix = "┣━"
                lines.append(f"   {prefix} {subtask.number}. {subtask.is_done_check} {subtask.name.title()}")
                lines.append(f"   ┃    Due: {subtask.due_date}")

        return '\n'.join(lines)


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

    def subtask_progress_bar(self):
        list_len = len(self.subtasks)
        subs_done = 0

        bar_fixed_width = 20

        if list_len != 0:
            bar_increment_value = round(bar_fixed_width / list_len)

            for i in self.subtasks:
                if i.is_done_check == '[X]':
                    subs_done += 1

            progress_percent = round((subs_done / list_len) * 100)

            progress_bar = ' ' * bar_fixed_width

            updated_progress_bar = progress_bar.replace(' ', '■', bar_increment_value*subs_done)
            return f'|{updated_progress_bar}| {progress_percent}%'
        else:
            return f'No Subtasks'

    def print_subtasks(self):
        for s in self.subtasks:
            print(s)

    def add_subtask(self, subtask):
        self.subtasks.append(subtask)

    def number_of_subs_complete(self):
        num_complete = 0
        for s in self.subtasks:
            if s.is_done_check == '[X]':
                num_complete += 1
        return num_complete
    
    def all_subtasks_complete(self):
        if not self.subtasks:
            return False  # Return False if there are no subtasks

        for subtask in self.subtasks:
            if not subtask.is_done_check == '[X]':
                return False  # Return False if any subtask is not complete
        return True  # Return True if all subtasks are complete
    #TODO: mark task as complete if all subtasks are completed
        
    def mark_as_completed(self):
        self.is_done_check = '[X]'

        with open(location) as json_file:
            data = json.load(json_file)

        for task in data['todoitems']:
            if task['number'] == self.number:
                task['is_done_check'] = '[X]'

        with open(location, 'w') as f:
            json.dump(data, f, indent=4)

    def mark_as_incomplete(self):
        self.is_done_check = '[ ]'

        with open(location) as json_file:
            data = json.load(json_file)

        for task in data['todoitems']:
            if task['number'] == self.number:
                task['is_done_check'] = '[ ]'

        with open(location, 'w') as f:
            json.dump(data, f, indent=4)

    def edit_name(self, edited_name):
        pass

    def edit_date(self, edited_date):
        pass

    def edit_classname(self, edited_classname):
        pass

    def remove_from_json(self):
        pass

    
