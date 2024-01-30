from abc import ABC, abstractmethod

class Task(ABC):
    def __init__(self, name, due_date, number, is_done_check='[ ]'):
        self.name = name
        self.due_date = due_date
        self.number = number
        self.is_done_check = is_done_check

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

