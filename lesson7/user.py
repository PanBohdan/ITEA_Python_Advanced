from mysql_handler import CursorHandler, ConnectionHandler
from constants import CONFIG


class User:
    def __init__(self, username, admin):
        self._username = username
        self._admin = admin

    def main_menu(self):
        if self._admin:
            self.admin_menu()
        else:
            self.user_menu()

    def admin_menu(self):
        print(f"Welcome {self._username}\n"
              'Admin Menu\n'
              '1 - Add student\n'
              '2 - Change student\n'
              '3 - Logout\n')
        inp = input()
        if inp == '1':
            faculty = input('Enter new student faculty ')
            group = input('Enter new student group ')
            stud_id = input('Enter new student id ')
            try:
                grade = int(input('Enter new student grade '))
                if not 1 >= grade <= 12:
                    with ConnectionHandler(**CONFIG) as ch:
                        with CursorHandler(ch) as cursor:
                            query = 'INSERT INTO students (id, faculty, student_group, student_id, grades) ' \
                                    f"VALUES (NULL, '{faculty}', '{group}', '{stud_id}', '{grade}')"
                            cursor.execute(query)
                else:
                    print('Grade must be in range from 1 to 12')
            except ValueError:
                print('Error: grade must be an integer')
        if inp == '2':
            inner_inp = input('Enter id of the student you want to change ')
            what_to_change = input('Select what you want to change:\n'
                                   '1 - faculty\n'
                                   '2 - group\n'
                                   '3 - id\n'
                                   '4 - grade\n')
            with ConnectionHandler(**CONFIG) as ch:
                with CursorHandler(ch) as cursor:
                    if what_to_change == '1':
                        new_faculty = input('Enter new faculty ')
                        query = f"UPDATE students SET faculty='{new_faculty}' " \
                                f"WHERE students.student_id='{inner_inp}'"
                        cursor.execute(query)
                        print('Done')
                    if what_to_change == '2':
                        new_group = input('Enter new group ')
                        query = f"UPDATE students SET student_group='{new_group}' " \
                                f"WHERE students.student_id='{inner_inp}'"
                        cursor.execute(query)
                        print('Done')
                    if what_to_change == '3':
                        new_stud_id = input('Enter new id ')
                        query = f"UPDATE students SET student_id='{new_stud_id}' " \
                                f"WHERE students.student_id='{inner_inp}'"
                        cursor.execute(query)
                        print('Done')
                    if what_to_change == '4':
                        try:
                            new_grade = int(input('Enter new grade '))
                            if not 1 >= new_grade <= 12:
                                query = f"UPDATE students SET grades='{new_grade}' " \
                                        f"WHERE students.student_id='{inner_inp}'"
                                cursor.execute(query)
                            else:
                                print('Grade must be in range from 1 to 12')
                        except ValueError:
                            print('Error: grade must be an integer')

                        print('Done')
        if inp == '3':
            return
        self.admin_menu()

    def user_menu(self):
        print(f"Welcome {self._username}\n"
              'User Menu\n'
              '1 - List of all students\n'
              '2 - List of best students\n'
              '3 - Find student by student id\n'
              '4 - Logout\n')
        inp = input()
        if inp == '1':
            with ConnectionHandler(**CONFIG) as ch:
                with CursorHandler(ch) as cursor:
                    query = 'SELECT * FROM students'
                    cursor.execute(query)
                    for _, faculty, student_group, student_id, grades in cursor:
                        print(f"faculty: {faculty}, group: {student_group}, "
                              f"id: {student_id}, grade: {grades}")
        if inp == '2':
            with ConnectionHandler(**CONFIG) as ch:
                with CursorHandler(ch) as cursor:
                    query = 'SELECT * FROM students WHERE grades > 9'
                    cursor.execute(query)
                    for _, faculty, student_group, student_id, grades in cursor:
                        print(f"faculty: {faculty}, group: {student_group}, "
                              f"id: {student_id}, grade: {grades}")
        if inp == '3':
            inner_inp = input('Enter student id ')
            with ConnectionHandler(**CONFIG) as ch:
                with CursorHandler(ch) as cursor:
                    query = f"SELECT * FROM students WHERE student_id='{inner_inp}'"
                    cursor.execute(query)
                    for _, faculty, student_group, student_id, grades in cursor:
                        print(f"Found student with id {inner_inp}\n"
                              f"faculty: {faculty}, group: {student_group}, "
                              f"grade: {grades}")
        if inp == '4':
            return
        self.user_menu()
