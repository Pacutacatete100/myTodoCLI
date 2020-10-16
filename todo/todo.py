import sys
import os
import click
from todo.TodoItem import Todo_Item
import todo.TodoItem
import datetime
import json
import calendar
import dateparser

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'secrets.txt')
with open(my_file) as f:
    location = f.readline()

todo_list = Todo_Item.load_objects_from_json()
current_date = datetime.date.today()
date_format_string = '%A %B %d %Y'
tomorrow_ = current_date + datetime.timedelta(days=1)
current_weekday = current_date.strftime('%A')
tomorrow_weekday = tomorrow_.strftime('%A')
weekday_dict = {'Monday': 1, 'Tuesday': 2, 'Wednesday': 3, 'Thursday': 4, 'Friday': 5, 'Saturday': 6, 'Sunday': 7}
weekdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
days_in_month = calendar.monthrange(current_date.year, current_date.month)


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
        click.echo(' - NO CLASSROOM')
        click.echo(' - RENA HILL')
        click.echo(' - ONLINE\n')


def print_list():
    new_list = Todo_Item.load_objects_from_json()
    click.echo('')
    click.echo(f'----- TODAY IS: {current_date.strftime(date_format_string).upper()} -----\n')
    click.echo('--------------- TODO LIST ------------------\n')
    for ti in new_list:
        click.echo(ti)
    print_day_schedule(current_weekday, 'today')


def process_date(due):
    if due in weekdays:
        last_weekday = dateparser.parse(due).strftime('%m-%d')
        last_weekday_nums = last_weekday.split('-')
        if (int(last_weekday_nums[1]) + 7) > days_in_month[1]:
            return 'kkl'
        else:
            next_weekday_num = int(last_weekday_nums[1]) + 7
            return f'{last_weekday_nums[0]}-{str(next_weekday_num)}'
    else:
        return due


@click.group('todo')
def main():
    pass


@main.command('list')
def list():
    print_list()


@main.command('add')
@click.option('--item', prompt='Enter the new Item')
@click.option('--due', prompt='Due Date in mm-dd format')
@click.option('--classname', prompt='Class Name')
def add(item, due, classname):
    processed_due_date = dateparser.parse(due).strftime(date_format_string)
    new_item = Todo_Item(item, processed_due_date, len(todo_list) + 1, class_name=classname)
    new_item.add_to_json(new_item, location)
    print_list()


@main.command('done')
@click.option('--num', prompt='Number of item you want to mark as completed or "all" to mark all items as completed')
def done(num):
    if num == 'all':
        Todo_Item.mark_all_complete()
    else:
        number = int(num)
        todo_list[number - 1].mark_as_completed()
    print_list()


@main.command('remove')
@click.option('--num', prompt='Number of item you want to remove or "done" to remove all the completed items')
def remove(num):
    if num == 'done':
        Todo_Item.remove_all_completed()
    else:
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


@main.command('edit')
@click.option('--num', prompt='the number of the item you want to edit')
@click.option('--part', prompt='enter what part you want to edit (item, date, class)')
@click.option('--edited', prompt='enter the edited part')
def edit(num, part, edited):
    number = int(num)
    todo_list[number - 1].edit(part, edited)
    print_list()


@main.command('classes')
@click.option('--day', prompt='today or tomorrow')
def classes(day):
    if day == 'today':
        print_day_schedule(current_weekday, day)
    elif day == 'tomorrow':
        print_day_schedule(tomorrow_weekday, day)


if __name__ == '__main__':
    main()
