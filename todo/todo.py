import sys
import click
from todo.TodoItem import Todo_Item
import datetime
import json
import calendar
import dateparser


todo_list = Todo_Item.load_objects_from_json()
current_date = datetime.date.today()
date_format_string = '%A %B %d %Y'
tomorrow_ = current_date + datetime.timedelta(days = 1)
current_weekday = current_date.strftime('%A')
tomorrow_weekday = tomorrow_.strftime('%A')

    
def print_day_schedule(weekday, day):
    if weekday == 'Monday':
        click.echo('')
        click.echo(f'-------- {day.upper()}S CLASSES -----------\n')
    
        click.echo('BUSINESS, LECTURE')
        click.echo(' - 8:00 a.m. to 9:15 a.m.')
        click.echo(' - DYSON 209')
        click.echo(' - DEBRA ZAMBITO')
        click.echo(' - IN-PERSON\n')
        
        click.echo('CMPT120, LECTURE')
        click.echo(' - 2:00 p.m. to 3:15 p.m.')
        click.echo(' - LOWELL THOMAS 133')
        click.echo(' - DONALD SCHWARTZ')
        click.echo(' - ONLINE\n')

    elif weekday == 'Tuesday':
        click.echo('')
        click.echo('-------- NO CLASSES TODAY -----------\n')

    elif weekday == 'Wednesday':
        click.echo(f'-------- {day.upper()}S CLASSES -----------\n')
        click.echo('ENG120, LECTURE')
        click.echo(' - 2:00 p.m. to 3:15 p.m.')
        click.echo(' - MUSIC 3203')
        click.echo(' - MOIRA FITZGIBBONS')
        click.echo(' - IN-PERSON\n')

    elif weekday == 'Thursday':
        click.echo('')
        click.echo(f'-------- {day.upper()}S CLASSES -----------\n')
        click.echo('PHIL, LECTURE')
        click.echo(' - 12:30 p.m. to 1:45 p.m.')
        click.echo(' - LOWELL THOMAS 006')
        click.echo(' - HENRY PRATT')
        click.echo(' - IN-PERSON\n')

        click.echo('CMPT120, LECTURE')
        click.echo(' - 2:00 p.m. to 3:15 p.m.')
        click.echo(' - LOWELL THOMAS 133')
        click.echo(' - DONALD SCHWARTZ')
        click.echo(' - IN_PERSON\n')

        click.echo('STATS, LECTURE')
        click.echo(' - 5:00 p.m. to 6:15 p.m.')
        click.echo(' - HANCOCK 2017')
        click.echo(' - ERIC BRADFORD')
        click.echo(' - IN-PERSON\n')

    elif weekday == 'Friday':
        click.echo(f'-------- {day.upper()}S CLASSES -----------\n')
        click.echo('BUSINESS, LECTURE')
        click.echo(' - 11:00 a.m. to 12:15 p.m.')
        click.echo(' - TBD')
        click.echo(' - RENA HILL')
        click.echo(' - IN-PERSON\n')

def print_list():
    new_list = Todo_Item.load_objects_from_json()
    click.echo('')
    click.echo(f'----- TODAY IS: {current_date.strftime(date_format_string).upper()} -----\n')
    click.echo('--------------- TODO LIST ------------------\n')
    for ti in new_list:
        click.echo(ti)
    print_day_schedule(current_weekday, 'today')


@click.group('todo')
def main():
    pass

@main.command('list') 
def list():
    print_list()

@main.command('add')
@click.option('--item', prompt=True)
@click.option('--due', prompt='Due Date in mm-dd format')
@click.option('--classname', prompt='Class Name')
def add(item, due, classname):
    due_date = dateparser.parse(due).strftime(date_format_string)
    new_item = Todo_Item(item, due_date, len(todo_list) + 1, class_name=classname)
    new_item.add_to_json(new_item, 'C:/Users/pacut/Desktop/Code/myTodoCLI/todo/todolist.json')
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
    click.echo(f'--------------- FOR {classname.upper()} ---------------\n')
    for i in todo_list:
        if i.class_name == classname:
            click.echo(i)

@main.command('date')
@click.option('--duedate', prompt='Date in mm-dd format')
def date(duedate):
    formatted_due_date = dateparser.parse(duedate).strftime(date_format_string)
    due_date_weekday = dateparser.parse(duedate).strftime('%A')
    click.echo('')
    click.echo(f'--------------- DUE {formatted_due_date.upper()} ---------------\n')
    for i in todo_list:
        if i.due_date == formatted_due_date:
            click.echo(i)
    print_day_schedule(due_date_weekday.capitalize(), due_date_weekday)

@main.command('today')
def today():
    click.echo('')
    click.echo(f'--------------- DUE TODAY, {current_date.strftime(date_format_string).upper()} ---------------\n')
    for i in todo_list:
        if i.due_date == current_date.strftime(date_format_string):
            click.echo(i)
    print_day_schedule(current_weekday, 'today')
    
@main.command('tomorrow')
def tomorrow():
    click.echo('')
    click.echo(f'--------------- DUE TOMORROW, {tomorrow_.strftime(date_format_string).upper()} ---------------\n')
    for i in todo_list:
        if i.due_date == tomorrow_.strftime(date_format_string):
            click.echo(i)
    print_day_schedule(tomorrow_weekday, 'tomorrow')

if __name__ == '__main__':
    main()
