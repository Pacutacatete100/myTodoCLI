import sys
import click
from TodoItem import Todo_Item
import datetime

todo_list = [Todo_Item(False, "Fill up this list", "tomorrow", 1), 
             Todo_Item(False, "another item for testing", "tomorrow", 2),
             Todo_Item(False, "100 pushups", "tomorrow", 3)
            ]

@click.group('todo')
def main():
    pass

@main.command('list') 
def list():
    click.echo('--------------- TODO LIST ---------------')
    for ti in todo_list:
        click.echo(ti)
    click.echo('')

@main.command('add')
@click.option('--item', prompt=True)
@click.option('--due', prompt=True)
@click.option('--classname', prompt='Class Name')
def add(item, due, classname):
    todo_list.append(Todo_Item(False, item, due, len(todo_list) + 1, classname))
    click.echo('------------ TODO LIST ------------')
    for ti in todo_list:
        click.echo(ti)
    click.echo('')

if __name__ == '__main__':
    main()