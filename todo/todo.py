import sys
import click
from TodoItem import Todo_Item
import datetime

initital_todo_list = [Todo_Item(False, "Fill up this list", "tomorrow", 1), 
                    Todo_Item(False, "another item for testing", "tomorrow", 2)
                    ]

@click.group('todo')
def main():
    pass

@main.command('list') 
def list():
    click.echo('--------------- TODO LIST ---------------')
    for ti in initital_todo_list:
        click.echo(ti)
    click.echo('')

@main.command('add')
@click.option('--item', prompt=True)
@click.option('--due', prompt=True)
def add(item, due):
    initital_todo_list.append(Todo_Item(False, item, due, len(initital_todo_list) + 1))
    click.echo('------------ TODO LIST ------------')
    for ti in initital_todo_list:
        click.echo(ti)
    click.echo('')
    

if __name__ == '__main__':
    main()