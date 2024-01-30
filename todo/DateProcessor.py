import datetime
import calendar
import dateparser

class DateProcessor:
    current_date = datetime.date.today()
    date_format_string = '%A %B %d %Y'
    tomorrow_ = current_date + datetime.timedelta(days=1)
    current_weekday = current_date.strftime('%A')
    tomorrow_weekday = tomorrow_.strftime('%A')
    weekdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    days_in_month = calendar.monthrange(current_date.year, current_date.month)
    current_month = current_date.strftime('%m')

    @staticmethod
    def process_date(due):
        if due in DateProcessor.weekdays:
            last_weekday = dateparser.parse(due).strftime('%m-%d')
            last_weekday_nums = last_weekday.split('-')

            if (int(last_weekday_nums[1]) + 7) > DateProcessor.days_in_month[1]: #if weekday entered is after end of month
                date_str = f'{int(DateProcessor.current_month) + 1}-{(int(last_weekday_nums[1]) + 7) - DateProcessor.days_in_month[1]}'
                return dateparser.parse(date_str).strftime(DateProcessor.date_format_string)

            elif due.upper() == DateProcessor.current_weekday.upper():
                date_str = f'{int(DateProcessor.current_month)}-{(int(last_weekday_nums[1]) + 7)}' #if weekday entered is same as current day 
                return dateparser.parse(date_str).strftime(DateProcessor.date_format_string)

            else:
                next_weekday_num = int(last_weekday_nums[1]) + 7
                date_str = f'{last_weekday_nums[0]}-{str(next_weekday_num)}'
                return dateparser.parse(date_str).strftime(DateProcessor.date_format_string)
        else:
            due = {'td': 'today', 'tm': 'tomorrow'}.get(due, due)
            return dateparser.parse(due).strftime(DateProcessor.date_format_string)
        
    @staticmethod
    def tomorrow():
        return DateProcessor.tomorrow_.strftime(DateProcessor.date_format_string)
    
    @staticmethod
    def today():
        return DateProcessor.current_date.strftime(DateProcessor.date_format_string)