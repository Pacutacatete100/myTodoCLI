import json
import orjson
import os

from todo.Course import Course

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'secrets.txt')
with open(my_file) as f:
    location = f.readline().strip('\n')

class CourseList:
    def __init__(self):
        self.courses = self.load_courses()
        self.possible_courses = ['NONE']

    def __iter__(self):
        return iter(self.courses)
    
    def __len__(self):
        return len(self.courses)
    
    def __getitem__(self, index):
        return self.courses[index]

    def load_courses(self):
        with open(location) as json_file:
            data = json.load(json_file)
            
        return [Course.dict_to_course(course) for course in data.get('courses', [])]

    def possible_courses(self):
        abbreviations = [course.abbreviation for course in self.courses]
        self.possible_courses.extend(abbreviations)

    def add_course(self, course):
        self.courses.append(course)
        course.add_course_to_json(location)

    def remove_course(self, course):
        self.courses.remove(course)
