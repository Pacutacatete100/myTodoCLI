class Todo_Item:
    def __init__(self, is_done, name, due_date, number, is_done_check):
        self.is_done = is_done
        self.name = name
        self.due_date = due_date
        self.number = number
        self.is_done_check = '[ ]'

    def __str__(self):
        return str(self.number) + '. ' + self.is_done_check + ' ' + self.name + ' is due ' + self.due_date

    def mark_as_completed(self):
        self.is_done_check = '[x]'
        self.is_done = True