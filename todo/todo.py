import os
import click
from todo.TodoItem import TodoItem
import datetime
import calendar
import dateparser
from colorama import Fore, Style
import openai
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate


THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'secrets.txt')
with open(my_file) as f:
    location = f.readline()
    openai_api_key = f.readline().strip()

my_LLM = OpenAI(openai_api_key)
print(my_LLM)


todo_list = TodoItem.load_objects_from_json()
current_date = datetime.date.today()
date_format_string = '%A %B %d %Y'
tomorrow_ = current_date + datetime.timedelta(days=1)
current_weekday = current_date.strftime('%A')
tomorrow_weekday = tomorrow_.strftime('%A')
weekdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
days_in_month = calendar.monthrange(current_date.year, current_date.month)
current_month = current_date.strftime('%m')

def get_llm_item_dict(sentence: str, class_list: str):
    prompt = PromptTemplate(
        input_variables=["sentence", "class_list"],
        template='You will be given a sentence that contains a To Do item, a date, and a class the item is for. Extract the data from the sentence and put it in a Python dictionary as outlined below:\n{\"name\": \"NAME HERE\", \"due_date\": \"DATE HERE\", \"class_name\": \"NAME HERE\"}\n\nThe following list is a list of the possible classes the item can be for:\n{class_list}\n\nWhen reading the sentence, interpret what class the item may fit under and make the value of  \"class_name\" the name of that class. If the class name is found, omit it from the \"name\" value of the item. If the class name is not found, make the class name value \"None\"\n\nSENTENCE: {sentence}'
    )
    chain = LLMChain(llm=my_LLM, prompt=prompt)
    return chain.run({
        'sentence': sentence,
        'class_list': class_list
    })

def async_classes():
    click.echo('')
    click.echo('\033[35;1m' + '-------- ASYNCHRONOUS CLASSES -----------\n')

    click.echo('\033[35;1m' + 'DISTRIBUTED SYSTEMS | DIST')
    click.echo('\033[35;1m' + ' - ZHEN HUANG')
    click.echo('\033[35;1m' + ' - ASYNCHRONOUS\n')

    click.echo('\033[0m' + '')


def print_day_schedule(weekday, day):
    if weekday == 'Monday':
        click.echo('')
        click.echo(click.style(f'-------- {day.upper()}S CLASSES -----------\n', fg='cyan'))

        click.echo(click.style('LATIN AMERICAN HISTORY | HIST', fg='cyan'))
        click.echo(click.style(' - 9:40 a.m. to 11:10 p.m.', fg='cyan'))
        click.echo(click.style(' - ARTS & LETTERS 406', fg='cyan'))
        click.echo(click.style(' - LINCOLN PARK CAMPUS', fg='cyan'))
        click.echo(click.style(' - JUAN MORA-TORRES', fg='cyan'))
        click.echo(click.style(' - IN-PERSON\n', fg='cyan'))

        click.echo(click.style('IMMIGRANT EXPERIENCES | LSP', fg='cyan'))
        click.echo(click.style(' - 1:00 p.m. to 2:30 p.m.', fg='cyan'))
        click.echo(click.style(' - LEVAN CENTER 404', fg='cyan'))
        click.echo(click.style(' - LOOP CAMPIS', fg='cyan'))
        click.echo(click.style(' - ZERRIN BULUT', fg='cyan'))
        click.echo(click.style(' - IN-PERSON\n', fg='cyan'))

        async_classes()

    elif weekday == 'Tuesday':
        click.echo('')
        click.echo(click.style(f'-------- {day.upper()}S CLASSES -----------\n', fg='cyan'))

        click.echo(click.style('DATABASE SYSTEMS | DATA', fg='cyan'))
        click.echo(click.style(' - 11:50 a.m. to 1:20 p.m.', fg='cyan'))
        click.echo(click.style(' - CDM 228', fg='cyan'))
        click.echo(click.style(' - LOOP CAMPUS', fg='cyan'))
        click.echo(click.style(' - ELIECER PERAZA ALAYA', fg='cyan'))
        click.echo(click.style(' - IN-PERSON\n', fg='cyan'))

        async_classes()

    elif weekday == 'Wednesday':
        click.echo('')
        click.echo(click.style(f'-------- {day.upper()}S CLASSES -----------\n', fg='cyan'))

        click.echo(click.style('LATIN AMERICAN HISTORY | HIST', fg='cyan'))
        click.echo(click.style(' - 9:40 a.m. to 11:10 p.m.', fg='cyan'))
        click.echo(click.style(' - ARTS & LETTERS 406', fg='cyan'))
        click.echo(click.style(' - LINCOLN PARK CAMPUS', fg='cyan'))
        click.echo(click.style(' - JUAN MORA-TORRES', fg='cyan'))
        click.echo(click.style(' - IN-PERSON\n', fg='cyan'))

        click.echo(click.style('IMMIGRANT EXPERIENCES | LSP', fg='cyan'))
        click.echo(click.style(' - 1:00 p.m. to 2:30 p.m.', fg='cyan'))
        click.echo(click.style(' - LEVAN CENTER 404', fg='cyan'))
        click.echo(click.style(' - LOOP CAMPIS', fg='cyan'))
        click.echo(click.style(' - ZERRIN BULUT', fg='cyan'))
        click.echo(click.style(' - IN-PERSON\n', fg='cyan'))

        async_classes()

    elif weekday == 'Thursday':
        click.echo('')
        click.echo(click.style(f'-------- {day.upper()}S CLASSES -----------\n', fg='cyan'))

        click.echo(click.style('DATABASE SYSTEMS | DATA', fg='cyan'))
        click.echo(click.style(' - 11:50 a.m. to 1:20 p.m.', fg='cyan'))
        click.echo(click.style(' - CDM 228', fg='cyan'))
        click.echo(click.style(' - LOOP CAMPUS', fg='cyan'))
        click.echo(click.style(' - ELIECER PERAZA ALAYA', fg='cyan'))
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
        if ti.due_date == current_date.strftime(date_format_string) and ti.is_done_check == "[ ]":
            click.echo(click.style(ti.__str__(), fg='red'))
            # click.echo('\033[31;1m' + ti.__str__()), convert al color to this format, more color options
        elif ti.is_done_check == '[X]':
            click.echo(click.style(ti.__str__(), fg='white'))
        elif ti.due_date == tomorrow_.strftime(date_format_string):
            click.echo(click.style(ti.__str__(), fg='yellow'))
        else:
            click.echo(ti)

    print_day_schedule(current_weekday, 'today')
    click.echo('-----------------------------------------\n')
    progress_bar()


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

def progress_bar():
    # progress bar based on the number of items in the todo list and the number of items that are done
    
    new_list = TodoItem.load_objects_from_json()
    list_len = len(new_list)
    num_items_done = 0

    bar_fixed_width = 40

    if list_len != 0:
        bar_increment_value = round(bar_fixed_width / list_len)

        for i in new_list:
            if i.is_done_check == '[X]':
                num_items_done += 1
        
        progress_percent = round((num_items_done / list_len) * 100)

        progress_bar = ' ' * bar_fixed_width

        updated_progress_bar = progress_bar.replace(' ', '=', bar_increment_value*num_items_done)

        click.echo(click.style(f'|{updated_progress_bar}| {progress_percent}%', fg='green'))

    else:
        click.echo('No Items In List')

    

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
    click.echo(get_llm_item_dict("bio lab 2 thursday", "Data Structures, Algorithms, Biology, Mexican History"))

    if due == 'td':
        due = 'today'
    elif due == 'tm':
        due = 'tomorrow'

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
