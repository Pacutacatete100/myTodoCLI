import os
import click
from todo.TodoItem import TodoItem
import datetime
import calendar
import dateparser
from colorama import Fore, Style

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'secrets.txt')
with open(my_file) as f:
    location = f.readline()

todo_list = TodoItem.load_objects_from_json()
current_date = datetime.date.today()
date_format_string = '%A %B %d %Y'
tomorrow_ = current_date + datetime.timedelta(days=1)
current_weekday = current_date.strftime('%A')
tomorrow_weekday = tomorrow_.strftime('%A')
weekdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
days_in_month = calendar.monthrange(current_date.year, current_date.month)
current_month = current_date.strftime('%m')

def async_classes():
    click.echo('')
    click.echo(click.style(f'-------- ASYNCHRONOUS CLASSES -----------\n', fg='yellow'))
        
    click.echo(click.style('APPLIED SOCIAL ENGINEERING | SOCENG', fg='yellow'))
    click.echo(click.style(' - ASYNCHRONOUS', fg='yellow'))
    click.echo(click.style(' - FILIPO SHAREVSKI\n', fg='yellow'))

    click.echo(click.style('INTRO TO WEB COMPUTING | WEB', fg='yellow'))
    click.echo(click.style(' - ASYNCHRONOUS', fg='yellow'))
    click.echo(click.style(' - JOSEPH MENDELSOHN', fg='yellow'))
    click.echo('')


def print_day_schedule(weekday, day):
    if weekday == 'Monday':
        click.echo('')
        click.echo(click.style(f'-------- {day.upper()}S CLASSES -----------\n', fg='cyan'))

        click.echo(click.style('ETHICS IN TECHNOLOGY | ETHICS', fg='cyan'))
        click.echo(click.style(' - 11:20 a.m. to 12:50 p.m.', fg='cyan'))
        click.echo(click.style(' - LEVAN CENTER 301', fg='cyan'))
        click.echo(click.style(' - EDWARD TVERDEK', fg='cyan'))
        click.echo(click.style(' - IN-PERSON\n', fg='cyan'))

        click.echo(click.style('INTRO TO CS | INTRO', fg='cyan'))
        click.echo(click.style(' - 3:10 p.m. to 4:40 p.m.', fg='cyan'))
        click.echo(click.style(' - CDM CENTER 220', fg='cyan'))
        click.echo(click.style(' - AMBER SETTLE', fg='cyan'))
        click.echo(click.style(' - IN-PERSON\n', fg='cyan'))

        async_classes()

    elif weekday == 'Tuesday':
        click.echo('')
        click.echo(click.style(f'-------- {day.upper()}S CLASSES -----------\n', fg='cyan'))

        click.echo(click.style('COMPOSITION & RHETORIC | RHET', fg='cyan'))
        click.echo(click.style(' - 11:50 a.m. to 1:20 p.m.', fg='cyan'))
        click.echo(click.style(' - LEWIS CENTER 1516', fg='cyan'))
        click.echo(click.style(' - CATHY MARTENSEN', fg='cyan'))
        click.echo(click.style(' - IN-PERSON\n', fg='cyan'))

        async_classes()

    elif weekday == 'Wednesday':
        click.echo('')
        click.echo(click.style(f'-------- {day.upper()}S CLASSES -----------\n', fg='cyan'))

        click.echo(click.style('ETHICS IN TECHNOLOGY | ETHICS', fg='cyan'))
        click.echo(click.style(' - 11:20 a.m. to 12:50 p.m.', fg='cyan'))
        click.echo(click.style(' - LEVAN CENTER 301', fg='cyan'))
        click.echo(click.style(' - EDWARD TVERDEK', fg='cyan'))
        click.echo(click.style(' - IN-PERSON\n', fg='cyan'))

        click.echo(click.style('INTRO TO CS | INTRO', fg='cyan'))
        click.echo(click.style(' - 3:10 p.m. to 4:40 p.m.', fg='cyan'))
        click.echo(click.style(' - CDM CENTER 220', fg='cyan'))
        click.echo(click.style(' - AMBER SETTLE', fg='cyan'))
        click.echo(click.style(' - IN-PERSON\n', fg='cyan'))

        async_classes()

    elif weekday == 'Thursday':
        click.echo('')
        click.echo(click.style(f'-------- {day.upper()}S CLASSES -----------\n', fg='cyan'))

        click.echo(click.style('COMPOSITION & RHETORIC | RHET', fg='cyan'))
        click.echo(click.style(' - 11:50 a.m. to 1:20 p.m.', fg='cyan'))
        click.echo(click.style(' - LEWIS CENTER 1516', fg='cyan'))
        click.echo(click.style(' - CATHY MARTENSEN', fg='cyan'))
        click.echo(click.style(' - IN-PERSON\n', fg='cyan'))

        async_classes()


    elif weekday == 'Friday':
        click.echo(f'-------- NO IN-PERSON CLASSES -----------\n')
        async_classes()
        

def print_list():
    new_list = TodoItem.load_objects_from_json()
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
        if (int(last_weekday_nums[1]) + 7) > days_in_month[1]: #if weekday entered is after end of month
            date_str = f'{int(current_month) + 1}-{(int(last_weekday_nums[1]) + 7) - days_in_month[1]}'
            return dateparser.parse(date_str).strftime(date_format_string)
        elif due.upper() == current_weekday.upper():
            date_str = f'{int(current_month)}-{(int(last_weekday_nums[1]) + 7)}' #if weekday entered is same as current day 
            return dateparser.parse(date_str).strftime(date_format_string)
        else:
            next_weekday_num = int(last_weekday_nums[1]) + 7
            date_str = f'{last_weekday_nums[0]}-{str(next_weekday_num)}'
            return dateparser.parse(date_str).strftime(date_format_string)
    else:
        return dateparser.parse(due).strftime(date_format_string)


@click.group('todo')
def main():
    pass


@main.command('list')
def list_():
    print_list()


@main.command('add')
@click.option('--item', prompt='Enter the new Item')
@click.option('--due', prompt='Due Date in mm-dd format')
@click.option('--classname', prompt='Class Name')
def add(item, due, classname):
    processed_due_date = process_date(due)
    new_item = TodoItem(item, processed_due_date, len(todo_list) + 1, class_name=classname)
    new_item.add_to_json(new_item, location)
    print_list()


@main.command('done')
@click.option('--num', prompt='Number of item you want to mark as completed or "all" to mark all items as completed')
def done(num):
    if num == 'all':
        TodoItem.mark_all_complete()
    else:
        number = int(num)
        todo_list[number - 1].mark_as_completed()
    print_list()


@main.command('remove')
@click.option('--num', prompt='Number of item you want to remove or "done" to remove all the completed items')
def remove(num):
    if num == 'done':
        TodoItem.remove_all_completed()
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
    formatted_due_date = process_date(duedate)
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

@main.command('async')
def async_classes_():
    async_classes()


if __name__ == '__main__':
    main()
