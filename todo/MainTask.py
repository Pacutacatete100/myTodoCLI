from todo.Task import Task
from todo.SubTask import SubTask
import ujson as json
import os
from colorama import Fore, Style
from todo.DateProcessor import DateProcessor


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
        lines = []

        # Determine color for main task
        if self.is_done_check == '[X]':
            due_date_color = Fore.GREEN
        else:
            if self.due_date == DateProcessor.today():
                due_date_color = Fore.RED
            elif self.due_date == DateProcessor.tomorrow():
                due_date_color = Fore.YELLOW
            else:
                due_date_color = Style.RESET_ALL

        lines.append(f" {due_date_color}{self.number}. {self.is_done_check} {self.name.title()}{Style.RESET_ALL}")
        lines.append(f"   {due_date_color}Due: {self.due_date.title()}, Class: {self.classname.upper()}{Style.RESET_ALL}")
        lines.append(f'   {due_date_color}┃{Style.RESET_ALL}')

        for i, subtask in enumerate(self.subtasks):
            # Determine color for subtask
            if subtask.is_done_check == '[X]':
                subtask_color = Fore.GREEN
            else:
                # Determine color for subtask due date
                if subtask.due_date == DateProcessor.current_date.strftime(DateProcessor.date_format_string): # if subtask due date is today
                    subtask_color = Fore.RED
                elif subtask.due_date == DateProcessor.tomorrow_.strftime(DateProcessor.date_format_string): # if subtask due date is tomorrow
                    subtask_color = Fore.YELLOW
                else:
                    subtask_color = Style.RESET_ALL

            if i == len(self.subtasks) - 1:  # Check if it's the last subtask
                prefix = f"{due_date_color}┗━{Style.RESET_ALL}"
                lines.append(f"   {prefix} {subtask_color}{subtask.number}. {subtask.is_done_check} {subtask.name.title()}{Style.RESET_ALL}")
                lines.append(f"        {subtask_color}Due: {subtask.due_date}{Style.RESET_ALL}")  # No vertical line for the last subtask
            else:
                prefix = f"{due_date_color}┣━{Style.RESET_ALL}"
                lines.append(f"   {prefix} {subtask_color}{subtask.number}. {subtask.is_done_check} {subtask.name.title()}{Style.RESET_ALL}")
                lines.append(f"   {due_date_color}┃{Style.RESET_ALL}    {subtask_color}Due: {subtask.due_date}{Style.RESET_ALL}")

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
        self.name = edited_name

        with open(location) as json_file:
            data = json.load(json_file)
        
        for task in data['todoitems']:
            if task['number'] == self.number:
                task['name'] = edited_name
        
        with open(location, 'w') as f:
            json.dump(data, f, indent=4)

    def edit_date(self, edited_date):
        self.name = edited_date

        with open(location) as json_file:
            data = json.load(json_file)
        
        for task in data['todoitems']:
            if task['number'] == self.number:
                task['due_date'] = edited_date
        
        with open(location, 'w') as f:
            json.dump(data, f, indent=4)

    def edit_classname(self, edited_classname):
        self.name = edited_classname

        with open(location) as json_file:
            data = json.load(json_file)
        
        for task in data['todoitems']:
            if task['number'] == self.number:
                task['classname'] = edited_classname
        
        with open(location, 'w') as f:
            json.dump(data, f, indent=4)

    def remove_from_json(self, number):
        with open(location) as json_file:
            data = json.load(json_file)

        if number == "done":
            # Remove all items that are marked as done
            data['todoitems'] = [item for item in data['todoitems'] if item['is_done_check'] != '[X]']
        else:
            # Remove a specific item by filtering
            number = int(number)
            data['todoitems'] = [item for item in data['todoitems'] if item['number'] != number]
            # Adjust the numbering for remaining items
        for i, item in enumerate(data['todoitems'], start=1):
            item['number'] = i

        # Write the updated data back to the JSON file
        with open(location, 'w') as json_file:
            json.dump(data, json_file, indent=4)

    
