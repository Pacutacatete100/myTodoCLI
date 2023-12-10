import os
import click
import datetime
import calendar
import dateparser
import openai
from langchain.llms import OpenAI

from todo.MainTask import MainTask
from todo.SubTask import SubTask
from todo.TaskController import TodoList

# secret info
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'secrets2.txt')
with open(my_file) as f:
    lines = f.readlines()
    location = lines[0].strip('\n')
    gpt_key = lines[1].strip('\n')

llm = OpenAI(openai_api_key=gpt_key)

todo_list = TodoList() #main todo list

# date processing variables
current_date = datetime.date.today()
date_format_string = '%A %B %d %Y'
tomorrow_ = current_date + datetime.timedelta(days=1)
current_weekday = current_date.strftime('%A')
tomorrow_weekday = tomorrow_.strftime('%A')
weekdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
days_in_month = calendar.monthrange(current_date.year, current_date.month)
current_month = current_date.strftime('%m')

# task item inference
def get_sentence_dict(sentence: str):

    response = openai.ChatCompletion.create(
        model="gpt-4-1106-preview",
        messages=[
            {
                "role": "system",
                "content": "You will be given a sentence that contains a To Do item, a date, and a class the item is for. Extract the data from the sentence and put it in the format outlined below:\n\n NAME OF ITEM\n DATE\n CLASS NAME\n\nOnly include the final values and omit any quotation marks, white spaces, new lines, commas, etc.\n\nThe following list is a list of the possible classes the item can be for:\nObject Oriented Programming, Concepts of Programming Languages, Science Fiction\n\nWhen reading the sentence, interpret what class the item may fit under and make the value of  \"CLASS NAME\" the name of that class. If the class name is found, omit it from the NAME OF ITEM value of the item. If the class name is not found, make the CLASS NAME value \"None\".\nIf the date has the name or part of the name of a month, interpret what number month it is and convert it into the \"MM-DD\" format.\nIf the date is the name of a weekday, \"today\", \"td\", \"tomorrow\", or \"tm\" leave it that way."
            },
            {
                "role": "user",
                "content": sentence
            }
        ],
    temperature=0,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)
    return response['choices'][0]['message']['content']

def async_classes():
    click.echo('')
    click.echo('\033[35;1m' + '-------- ASYNCHRONOUS CLASSES -----------\n')

    click.echo('\033[35;1m' + 'OBJECT ORIENTED SOFTWARE DEVELOPMENT | OBJ')
    click.echo('\033[35;1m' + ' - ASYNCHRONOUS')
    click.echo('\033[35;1m' + ' - CHRISTOPHER HIELD')
    click.echo('\033[35;1m' + ' - LIVE LECTURES HELD MONDAY & WEDNESDAY 11:50 a.m. to 1:20 p.m.')

    click.echo('\033[0m' + '')


def print_day_schedule(weekday, day):
    if weekday == 'Monday':
        click.echo('')
        click.echo(click.style(f'-------- {day.upper()}S CLASSES -----------\n', fg='cyan'))

        click.echo(click.style('PROGRAMMING LANGUAGE CONCEPTS | LANG', fg='cyan'))
        click.echo(click.style(' - 11:50 a.m. to 1:20 p.m.', fg='cyan'))
        click.echo(click.style(' - CDM CENTER 218', fg='cyan'))
        click.echo(click.style(' - LOOP CAMPUS', fg='cyan'))
        click.echo(click.style(' - CORIN PITCHER', fg='cyan'))
        click.echo(click.style(' - IN-PERSON\n', fg='cyan'))

        async_classes()

    elif weekday == 'Tuesday':
        click.echo('')
        click.echo(click.style(f'-------- {day.upper()}S CLASSES -----------\n', fg='cyan'))

        click.echo(click.style('SCIENDE FICTION | SCI', fg='cyan'))
        click.echo(click.style(' - 2:40 p.m. to 4:10 p.m.', fg='cyan'))
        click.echo(click.style(' - ARTS AND LETTERS HALL 201', fg='cyan'))
        click.echo(click.style(' - LINCOLN PARK CAMPUS', fg='cyan'))
        click.echo(click.style(' - REBECCA JOHNS-TRISSLER', fg='cyan'))
        click.echo(click.style(' - IN-PERSON\n', fg='cyan'))

        async_classes()

    elif weekday == 'Wednesday':
        click.echo('')
        click.echo(click.style(f'-------- {day.upper()}S CLASSES -----------\n', fg='cyan'))

        click.echo(click.style('PROGRAMMING LANGUAGE CONCEPTS | LANG', fg='cyan'))
        click.echo(click.style(' - 11:50 a.m. to 1:20 p.m.', fg='cyan'))
        click.echo(click.style(' - CDM CENTER 218', fg='cyan'))
        click.echo(click.style(' - LOOP CAMPUS', fg='cyan'))
        click.echo(click.style(' - CORIN PITCHER', fg='cyan'))
        click.echo(click.style(' - IN-PERSON\n', fg='cyan'))

        async_classes()

    elif weekday == 'Thursday':
        click.echo('')
        click.echo(click.style(f'-------- {day.upper()}S CLASSES -----------\n', fg='cyan'))

        click.echo(click.style('SCIENDE FICTION | SCI', fg='cyan'))
        click.echo(click.style(' - 2:40 p.m. to 4:10 p.m.', fg='cyan'))
        click.echo(click.style(' - ARTS AND LETTERS HALL 201', fg='cyan'))
        click.echo(click.style(' - LINCOLN PARK CAMPUS', fg='cyan'))
        click.echo(click.style(' - REBECCA JOHNS-TRISSLER', fg='cyan'))
        click.echo(click.style(' - IN-PERSON\n', fg='cyan'))

        async_classes()



    elif weekday == 'Friday':
        click.echo(f'-------- NO IN-PERSON CLASSES -----------\n')
        async_classes()
        
def print_list():

    print('#####  DEV VERSION  #####')
    new_list = TodoList()
    print('')
    click.echo(f'----- TODAY IS: {current_date.strftime(date_format_string).upper()} -----\n')
    click.echo('--------------- TODO LIST ------------------\n')
    
    for ti in new_list:
        if ti.due_date == current_date.strftime(date_format_string) and ti.is_done_check == "[ ]":
            click.echo(click.style(ti.str_with_bar(), fg='red') + '\n')
            # click.echo('\033[31;1m' + ti.__str__()), convert al color to this format, more color options
        elif ti.is_done_check == '[X]':
            click.echo(click.style(ti.str_with_bar(), fg='white') + '\n')
        elif ti.due_date == tomorrow_.strftime(date_format_string):
            click.echo(click.style(ti.str_with_bar(), fg='yellow') + '\n')
        else:
            print(ti.str_with_bar(),'\n')
    
    print_day_schedule(current_weekday, 'today')
    click.echo('----------------------------------------\n')
    new_list.main_progress_bar()


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


# CLI Commands
@click.group('todo')
def main():
    pass


@main.command('list')
def list_():
    print_list()


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
        generated_items = get_sentence_dict(item).splitlines()
        item, due, classname = generated_items

    due = {'td': 'today', 'tm': 'tomorrow'}.get(due, due)
    processed_due_date = process_date(due)

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
        print('AI not yet supported')

    due = {'td': 'today', 'tm': 'tomorrow'}.get(due, due)
    processed_due_date = process_date(due)

    new_subtask = SubTask(item, processed_due_date, len(todo_list[number - 1].subtasks) + 1)

    todo_list.add_sub(new_subtask, number-1)
    # new_subtask.add_sub_to_json(location, number-1)

    click.echo(todo_list[number -1].expanded_view())
    #TODO change to only thing here is adding to todolist
    #  - that add should update add it to the JSON

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
