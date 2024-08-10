import json
import orjson

class Course:
    def __init__(self, full_name, abbreviation, time, days, meeting_place, professor, online=False):
        self.full_name = full_name
        self.abbreviation = abbreviation
        self.time = time
        self.days = days
        self.meeting_place = meeting_place
        self.professor = professor
        self.online = online

    def __str__(self):
        return f'\n{self.full_name} | {self.abbreviation}\n - {self.time}\n - {self.meeting_place}\n - {self.professor}\n - {self.online}'
    
    def to_dict(self):
        return {
            'full_name': self.full_name,
            'abbreviation': self.abbreviation,
            'time': self.time,
            'days': self.days,
            'meeting_place': self.meeting_place,
            'professor': self.professor,
            'online': self.online
        }
    
    @staticmethod
    def dict_to_course(course_dict):
        return Course(
            full_name=course_dict['full_name'],
            abbreviation=course_dict['abbreviation'],
            time=course_dict['time'],
            days=course_dict['days'],
            meeting_place=course_dict['meeting_place'],
            professor=course_dict['professor'],
            online=course_dict['online']
        )
    
    def add_course_to_json(self, location):
        with open(location) as json_file:
            data = json.load(json_file)

        temp = data['courses']
        course_dict = self.__dict__
        temp.append(course_dict)
        
        with open(location, 'w') as f:
            json.dump(data, f, indent=4)

