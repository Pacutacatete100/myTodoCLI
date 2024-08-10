import click
import datetime
import calendar
import dateparser

from todo.MainTask import MainTask
from todo.SubTask import SubTask
from todo.TaskController import TodoList
from todo.DateProcessor import DateProcessor
from todo.Inference import Inference
from todo.CourseController import CourseList
from todo.Course import Course

todo_list = TodoList() #main todo list
courses_list = CourseList() #main course list

# date processing variables
current_date = datetime.date.today()
date_format_string = '%A %B %d %Y'
tomorrow_ = current_date + datetime.timedelta(days=1)
current_weekday = current_date.strftime('%A')
tomorrow_weekday = tomorrow_.strftime('%A')
weekdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
days_in_month = calendar.monthrange(current_date.year, current_date.month)
current_month = current_date.strftime('%m')

inferece = Inference()

def async_classes():
    click.echo('')
    click.echo('\033[35;1m' + '-------- ASYNCHRONOUS CLASSES -----------\n')

    click.echo('\033[35;1m' + 'COMPILER DESIGN | COMP')
    click.echo('\033[35;1m' + ' - ASYNCHRONOUS')
    click.echo('\033[35;1m' + ' - JOSEPH PHILLIPS')
    click.echo('\033[35;1m' + ' - NO LIVE LECTURES')
    click.echo('')

    click.echo(click.style('HISTORY OF WESTERN SCIENCE | HIST', fg='cyan'))
    click.echo(click.style(' - 9:40 a.m. to 11:10 p.m.', fg='cyan'))
    click.echo(click.style(' - ASYNC UNTIL MAY 1st', fg='cyan'))
    click.echo(click.style(' - CHRISTOPHER MARTINUZZI', fg='cyan'))
    click.echo(click.style(' - ONLINE\n', fg='cyan'))
    click.echo('')

    click.echo('\033[0m' + '')


def print_day_schedule(weekday, day):
    if weekday == 'Monday':
        click.echo('')
        click.echo(click.style(f'-------- {day.upper()}S CLASSES -----------\n', fg='cyan'))

        click.echo(click.style('HISTORY OF WESTERN SCIENCE | HIST', fg='cyan'))
        click.echo(click.style(' - 9:40 a.m. to 11:10 p.m.', fg='cyan'))
        click.echo(click.style(' - ASYNC UNTIL MAY 1st', fg='cyan'))
        click.echo(click.style(' - CHRISTOPHER MARTINUZZI', fg='cyan'))
        click.echo(click.style(' - ONLINE\n', fg='cyan'))
        click.echo('')

        click.echo(click.style('OBJECT ORIENTED ENTERPRISE APPLICATION DEVELOPMENT | ENTER', fg='cyan'))
        click.echo(click.style(' - 5:45 p.m. to 9:00 p.m.', fg='cyan'))
        click.echo(click.style(' - ONLINE LECTURE', fg='cyan'))
        click.echo(click.style(' - KEN YU', fg='cyan'))

        async_classes()

    elif weekday == 'Tuesday':
        click.echo(f'-------- NO IN-PERSON CLASSES -----------\n')
        async_classes()

    elif weekday == 'Wednesday':
        click.echo('')
        click.echo(click.style(f'-------- {day.upper()}S CLASSES -----------\n', fg='cyan'))

        click.echo(click.style('HISTORY OF WESTERN SCIENCE | HIST', fg='cyan'))
        click.echo(click.style(' - 9:40 a.m. to 11:10 p.m.', fg='cyan'))
        click.echo(click.style(' - ASYNC UNTIL MAY 1st', fg='cyan'))
        click.echo(click.style(' - CHRISTOPHER MARTINUZZI', fg='cyan'))
        click.echo(click.style(' - ONLINE\n', fg='cyan'))
        click.echo('')

        async_classes()

    elif weekday == 'Thursday':
        click.echo(f'-------- NO IN-PERSON CLASSES -----------\n')
        async_classes()

    elif weekday == 'Friday':
        click.echo(f'-------- NO IN-PERSON CLASSES -----------\n')
        async_classes()
        
def print_list():

    print('#####  DEV VERSION  #####')
    print('')
    click.echo(f'----- TODAY IS: {current_date.strftime(date_format_string).upper()} -----\n')
    click.echo('--------------- TODO LIST ------------------\n')

    for ti in todo_list:
        click.echo(ti.str_with_bar() + '\n')
    
    print_day_schedule(current_weekday, 'today')
    click.echo('----------------------------------------\n')
    todo_list.main_progress_bar()

# CLI Commands
@click.group('todo')
def main():
    pass


@main.command('list')
def list_():
    print_list()

    
@main.command('courses')
def courses():
    for c in courses_list:
        click.echo(c)

@main.command('add')
@click.option('-m', is_flag=True)
def add(m):
    if m:  # manual mode
        click.echo(click.style('MANUAL MODE', fg='yellow'))

        item = click.prompt('Enter the new Item')
        due = click.prompt('Due Date in mm-dd format')
        classname = click.prompt('Enter the Class name')

    else:  # inference mode
        # TODO: Exception handling when generated format not correct
        item = click.prompt('Enter the new Item')
        generated_items = inferece.get_main_task_data(item).split('\n')
        item, due, classname = generated_items

    processed_due_date = DateProcessor.process_date(due)

    new_item = MainTask(item, processed_due_date, len(todo_list) + 1, classname=classname)

    todo_list.add(new_item)
    print_list()
    
@main.command('addsub')
@click.option('--num', prompt='number of item you want to add a subtask to')
@click.option('-m', is_flag=True)
def addsub(num, m):
    number = int(num)
    if m:
        click.echo(click.style('MANUAL MODE', fg='yellow'))

        item = click.prompt('Enter the new Item')
        due = click.prompt('Due Date in mm-dd format')
    else:
        item = click.prompt('Enter the new Item')
        generated_items = inferece.get_subtask_data(item).split('\n')
        item, due = generated_items

    processed_due_date = DateProcessor.process_date(due)

    new_subtask = SubTask(item, processed_due_date, len(todo_list[number - 1].subtasks) + 1)

    todo_list.add_sub(new_subtask, number-1)

    click.echo(todo_list[number -1].expanded_view())

@main.command('subs')
@click.option('--num', prompt='What number item do you want to see the subtasks of')
def subs(num):
    number = int(num)
    click.echo(todo_list[number-1].expanded_view())

@main.command('subdone')
@click.option('--item', prompt='What number item do you want to mark a subtask as complete')
@click.option('--sub', prompt='What number sub task do you want to mark complete')
def subdone(item, sub):
    item_number = int(item)
    sub_number = int(sub)
    todo_list.sub_done(item_number, sub_number)
    print_list()

@main.command('subundone')
@click.option('--item', prompt='What number item do you want to mark a subtask as incomplete')
@click.option('--sub', prompt='What number sub task do you want to mark incomplete')
def subundone(item, sub):
    item_number = int(item)
    sub_number = int(sub)
    todo_list.sub_undone(item_number, sub_number)
    print_list()

@main.command('removesub')
@click.option('--item', prompt='What number item do you want to remove a subtask from')
@click.option('--sub', prompt='What number sub task do you want to remove')
def removesub(item, sub):
    item_number = int(item)
    todo_list.remove_sub(item_number, sub)
    click.echo(todo_list[item_number-1].expanded_view())

@main.command('done')
@click.option('--num', prompt='Number of item you want to mark as completed or "all" to mark all items as completed')
def done(num):
    number = int(num)
    todo_list.done(number)
    print_list()


@main.command('remove')
@click.option('--num', prompt='Number of item you want to remove or "done" to remove all the completed items')
def remove(num):
    todo_list.remove(num)
    print_list()


@main.command('undone')
@click.option('--num', prompt='number of item you want to mark as incomplete')
def undone(num):
    number = int(num)
    todo_list.undone(number)
    print_list()


@main.command('class')
@click.option('--classname', prompt='class you want to sort by')
def class_(classname):
    click.echo('')
    click.echo(f'--------------- FOR {classname.upper()} ---------------\n')
    for i in todo_list:
        if i.class_name == classname:

            if i.due_date == tomorrow_.strftime(date_format_string):
                click.echo(click.style(i.__str__(), fg='yellow'))

            elif i.due_date == current_date.strftime(date_format_string):
                click.echo(click.style(i.__str__(), fg='red'))
            else:
                click.echo(i)


@main.command('date')
@click.option('--duedate', prompt='Date in mm-dd format')
def date(duedate):
    formatted_due_date = DateProcessor.process_date(duedate)
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
            click.echo(click.style(i.__str__(), fg='red'))
    print_day_schedule(current_weekday, 'today')


@main.command('tomorrow')
def tomorrow():
    click.echo('')
    click.echo(f'--------------- DUE TOMORROW, {tomorrow_.strftime(date_format_string).upper()} ---------------\n')
    for i in todo_list:
        if i.due_date == tomorrow_.strftime(date_format_string):
            click.echo(click.style(i.__str__(), fg='yellow'))
    print_day_schedule(tomorrow_weekday, 'tomorrow')


@main.command('edit')
def edit():
    num = click.prompt('the number of the item you want to edit')
    
    valid_parts = ('item', 'date', 'class')
    def validate_part(part):
        if part not in valid_parts:
            raise click.BadParameter(f'part must be "item", "date", or "class"')
        return part

    number = int(num)
    while True:
        part = click.prompt('enter what part you want to edit (item, date, class)', type=str, value_proc=validate_part)
        if part:
            break

    edited = click.prompt('enter the edited part')
    todo_list.edit(number, part, edited)
    print_list()

@main.command('editsub')
def editsub(item, sub, part, edited):
    item = click.prompt('the number of the item you want to edit')
    sub = click.prompt('the number of the subtask you want to edit')
    valid_parts = ('item', 'date')
    def validate_part(part):
        if part not in valid_parts:
            raise click.BadParameter(f'part must be "item" or "date"')
        return part
    
    while True:
        part = click.prompt('enter what part you want to edit (item, date)', type=str, value_proc=validate_part)
        if part:
            break
    edited = click.prompt('enter the edited part')
    
    item_number = int(item)
    sub_number = int(sub)
    todo_list.edit_sub(item_number, sub_number, part, edited)
    click.echo(todo_list[item_number-1].expanded_view())


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

@main.command('addcourse')
def addcourse():
    course_name = click.prompt('Enter the new Course Name')
    course_abbrev = click.prompt('Enter the Course Abbreviation')
    course_time = click.prompt('Enter the Course Time')
    course_days = click.prompt('Enter the Course Week Days')
    course_location = click.prompt('Enter the Course Location')
    course_prof = click.prompt('Enter the Course Professor')
    course_online = click.prompt('Is the Course Online?')

    course = Course(course_name.upper(), course_abbrev.upper(), course_time, course_days.upper(), course_location.upper(), course_prof.upper(), course_online)
    courses_list.add_course(course)
    for c in courses_list:
        click.echo(c)


if __name__ == '__main__':
    main()
