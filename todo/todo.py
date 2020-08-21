import sys
import click
from TodoItem import Todo_Item
import datetime
import json
import calendar

todo_list = Todo_Item.load_objects_from_json()

def print_list():
    new_list = Todo_Item.load_objects_from_json()
    click.echo('--------------- TODO LIST ---------------')
    for ti in new_list:
        click.echo(ti)
    click.echo('')

@click.group('todo')
def main():
    pass

@main.command('list') 
def list():
    print_list()

@main.command('add')
@click.option('--item', prompt=True)
@click.option('--due', prompt=True)
@click.option('--classname', prompt='Class Name')
def add(item, due, classname):
    new_item = Todo_Item(item, due, len(todo_list) + 1, class_name=classname)
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
    click.echo(f'--------------- FOR {classname.upper()} ---------------')
    for i in todo_list:
        if i.class_name == classname:
            click.echo(i)
    click.echo('')

@main.command('date')
@click.option('--duedate', prompt='due date you want to sort by')
def date(duedate):
    click.echo(f'--------------- DUE {duedate.upper()} ---------------')
    for i in todo_list:
        if i.due_date == duedate:
            click.echo(i)
    click.echo('')

@main.command('today')
def today():
    click.echo('--------------- DUE TODAY ---------------')
    for i in todo_list:
        if i.due_date == 'today':
            click.echo(i)
    click.echo('')

@main.command('tomorrow')
def tomorrow():
    click.echo('--------------- DUE TOMORROW ---------------')
    for i in todo_list:
        if i.due_date == 'tomorrow':
            click.echo(i)
    click.echo('')

if __name__ == '__main__':
    main()