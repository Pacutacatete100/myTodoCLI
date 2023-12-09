from todo.Task import Task
import ujson as json

class SubTask(Task):
    # TODO: Complete implementation of subtask

    def __init__(self, name, due_date, number, is_done_check='[ ]'):
        self.name = name
        self.due_date = due_date
        self.number = number
        self.is_done_check = is_done_check

    def __str__(self) -> str:
        return f' {str(self.number)}. {self.is_done_check} {self.name.title()}\n   Due: {self.due_date.title()}'
    
    def to_dict(self):
        return {
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
    
    @staticmethod
    def dict_to_subtask(sub_dict_list):
        return [
            SubTask(
                name=subtask_dict['name'],
                due_date=subtask_dict['due_date'],
                number=subtask_dict['number'],
                is_done_check=subtask_dict.get('is_done_check', '[ ]')
            ) for subtask_dict in sub_dict_list
        ]
    
    def subtask_progress_bar(self):
        pass

    def mark_as_completed(self):
        pass

    def mark_as_incomplete(self):
        pass

    def edit_name(self, edited_name):
        pass

    def edit_date(self, edited_date):
        pass

    def add_to_json(self):
        pass

    def remove_from_json(self):
        pass

    