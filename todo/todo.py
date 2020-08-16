import sys
import click
from TodoItem import Todo_Item
import datetime
import json

todo_list = Todo_Item.load_objects_from_json()

def print_list():
    click.echo('--------------- TODO LIST ---------------')
    for ti in todo_list:
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
    todo_list.append(Todo_Item(False, item, due, len(todo_list) + 1, classname))
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
    todo_list.remove(todo_list[number - 1])
    #! make numbers shift to correct position
    print_list()

@main.command('undone')
@click.option('--num', prompt='number of item you want to mark as incomplete')
def undone(num):
    number = int(num)
    todo_list[number - 1].mark_as_incomplete()
    print_list()



if __name__ == '__main__':
    main()