import sys
import click
from TodoItem import Todo_Item
import datetime
import json
import calendar
import dateparser


todo_list = Todo_Item.load_objects_from_json()
current_date = datetime.date.today()
date_format_string = '%A %B %d %Y'
tomorrow_ = current_date + datetime.timedelta(days = 1)
current_weekday = current_date.strftime('%A')

print(current_weekday)

def print_list():
    new_list = Todo_Item.load_objects_from_json()
    click.echo('')
    click.echo('--------------- TODO LIST ------------------')
    click.echo(f'----- TODAY IS: {current_date.strftime(date_format_string).upper()} -----')
    click.echo('')
    for ti in new_list:
        click.echo(ti)
    

@click.group('todo')
def main():
    pass

@main.command('list') 
def list():
    print_list()

@main.command('add')
@click.option('--item', prompt=True)
@click.option('--due', prompt='Due Date: mm-dd')
@click.option('--classname', prompt='Class Name')
def add(item, due, classname):
    due_date = dateparser.parse(due).strftime(date_format_string)
    new_item = Todo_Item(item, due_date, len(todo_list) + 1, class_name=classname)
    new_item.add_to_json(new_item, 'todolist.json')
    print_list()

@main.command('done')
@click.option('--num', prompt='Number of item you want to mark as completed')
def done(num):
    number = int(num)
    todo_list[number - 1].mark_as_completed()
    print_list()

@main.command('remove')
@click.option('--num', prompt='Number of item you want to remove')
def remove(num):
    number = int(num)
    todo_list[number - 1].remove_from_json(number)
    print_list()

@main.command('undone')
@click.option('--num', prompt='number of item you want to mark as incomplete')
def undone(num):
    number = int(num)
    todo_list[number - 1].mark_as_incomplete()
    print_list()

@main.command('class')
@click.option('--classname', prompt='class you want to sort by')
def class_(classname):
    click.echo('')
    click.echo(f'--------------- FOR {classname.upper()} ---------------')
    for i in todo_list:
        if i.class_name == classname:
            click.echo(i)

@main.command('date')
@click.option('--duedate', prompt='Date in mm-dd format')
def date(duedate):
    formatted_due_date = dateparser.parse(duedate).strftime(date_format_string)
    click.echo('')
    click.echo(f'--------------- DUE {formatted_due_date.upper()} ---------------')
    for i in todo_list:
        if i.due_date == formatted_due_date:
            click.echo(i)

@main.command('today')
def today():
    click.echo('')
    click.echo(f'--------------- DUE TODAY, {current_date.strftime(date_format_string).upper()} ---------------')
    click.echo('')
    for i in todo_list:
        if i.due_date == current_date.strftime(date_format_string):
            click.echo(i)

@main.command('tomorrow')
def tomorrow():
    click.echo('')
    click.echo(f'--------------- DUE TOMORROW, {tomorrow_.strftime(date_format_string).upper()} ---------------')
    click.echo('')
    for i in todo_list:
        if i.due_date == tomorrow_.strftime(date_format_string):
            click.echo(i)

if __name__ == '__main__':
    main()