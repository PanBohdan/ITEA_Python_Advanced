from abc import ABC, abstractmethod
from datetime import date
import time

cur_time_1 = time.time()
our_list = []
for j in range(1000):
    our_list.append(j)

fin_time_1 = time.time() - cur_time_1
cur_time_2 = time.time()
other_list = [x for x in range(1000)]
fin_time_2 = time.time() - cur_time_2
print(fin_time_1, fin_time_2)


class Person:

    def __init__(self, surname, date_of_birth):
        self._surname = surname
        self._date_of_birth = date_of_birth

    @abstractmethod
    def get_surname(self):
        return self._surname

    @abstractmethod
    def get_age(self):
        today = date.today()
        age = today.year - self._date_of_birth.year - \
            ((today.month, today.day) < (self._date_of_birth.month,
                                         self._date_of_birth.day))
        return age


class Abiturient(Person):

    def __init__(self, surname, date_of_birth, faculty):
        self._surname = surname
        self._date_of_birth = date_of_birth
        self._faculty = faculty

    def get_surname(self):
        return self._surname+' is abiturient'

    def get_age(self):
        return super().get_age()

    def get_faculty(self):
        return self._faculty


class Student(Person):

    def __init__(self, surname, date_of_birth, faculty, course):
        self._surname = surname
        self._date_of_birth = date_of_birth
        self._faculty = faculty
        self._course = course

    def get_surname(self):
        return self._surname+' is student'

    def get_age(self):
        return super().get_age()

    def get_faculty(self):
        return self._faculty

    def get_course(self):
        return self._course


class Lecturer(Person):

    def __init__(self, surname, date_of_birth, faculty, experience):
        self._surname = surname
        self._date_of_birth = date_of_birth
        self._faculty = faculty
        self._experience = experience

    def get_surname(self):
        return self._surname+f" is lector with experience of " \
                             f"{self.get_experience()}"

    def get_age(self):
        return super().get_age()

    def get_faculty(self):
        return self._faculty

    def get_experience(self):
        return self._experience


list_of_persons = [Abiturient('Panko', date(2003, 1, 12),
                              'some faculty'),
                   Lecturer('Lecturer surname', date(1988, 5, 6),
                            'other faculty', '5 years'),
                   Student('Student surname', date(2000, 2, 12),
                           'other faculty', 'some course'),
                   Lecturer('Other lecturer surname', date(1900, 4, 13),
                            'some faculty', 'many years')]

our_age = 25
new_list = [x for x in list_of_persons if x.get_age() > our_age]
print(new_list)
list_of_names = [x.get_surname() for x in new_list]
print(list_of_names)
