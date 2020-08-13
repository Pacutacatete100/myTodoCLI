class Todo_Item:
    def __init__(self, is_done, name, due_date, number, class_name='misc', is_done_check='[ ]'):
        self.is_done = is_done
        self.name = name
        self.due_date = due_date
        self.number = number
        self.is_done_check = is_done_check if is_done_check is not None else '[ ]'
        self.class_name = class_name if class_name is not None else 'misc'

    def __str__(self):
        return str(self.number) + '. ' + self.is_done_check + ' ' + self.name + '. Due: ' + self.due_date + '. Class: ' + self.class_name

    def mark_as_completed(self):
        self.is_done_check = '[x]'
        self.is_done = True

    def mark_as_incomplete(self):
        self.is_done_check = '[ ]'
        self.is_done = False