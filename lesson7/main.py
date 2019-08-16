import mysql.connector
import hashlib
from getpass import getpass


config = {
  'user': 'root',
  'password': 'ThatSomeStrongPassword',
  'host': 'localhost',
  'database': 'student_db',
  'raise_on_warnings': True
}


class ConnectionHandler:
    def __init__(self, **cfg):
        self._config = cfg

    def __enter__(self):
        self.cnx = mysql.connector.connect(**self._config)
        return self.cnx

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.cnx.rollback()
        else:
            self.cnx.commit()
        self.cnx.close()


class CursorHandler:
    def __init__(self, our_connection):
        self.our_connection = our_connection

    def __enter__(self):
        self.our_cursor = self.our_connection.cursor(buffered=True)
        return self.our_cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.our_cursor.close()


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
                    with ConnectionHandler(**config) as ch:
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
            with ConnectionHandler(**config) as ch:
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
            with ConnectionHandler(**config) as ch:
                with CursorHandler(ch) as cursor:
                    query = 'SELECT * FROM students'
                    cursor.execute(query)
                    for _, faculty, student_group, student_id, grades in cursor:
                        print(f"faculty: {faculty}, group: {student_group}, "
                              f"id: {student_id}, grade: {grades}")
        if inp == '2':
            with ConnectionHandler(**config) as ch:
                with CursorHandler(ch) as cursor:
                    query = 'SELECT * FROM students WHERE grades > 9'
                    cursor.execute(query)
                    for _, faculty, student_group, student_id, grades in cursor:
                        print(f"faculty: {faculty}, group: {student_group}, "
                              f"id: {student_id}, grade: {grades}")
        if inp == '3':
            inner_inp = input('Enter student id ')
            with ConnectionHandler(**config) as ch:
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


def hashing_input(inp):
    our_hash = hashlib.md5(inp.encode())
    return our_hash.hexdigest()


def register():
    inp_username = input('Enter username: ')
    if inp_username.count(' ') >= 1:
        raise ValueError('Username cannot contain spaces')
    elif len(inp_username) == 0:
        raise ValueError('Username cannot be empty')
    with ConnectionHandler(**config) as ch:
        with CursorHandler(ch) as cursor:
            query = 'SELECT * FROM users WHERE 1'
            cursor.execute(query)
            list_of_usernames = []
            for (_, username, *_) in cursor:
                list_of_usernames.append(username)

    if inp_username in list_of_usernames:
        raise ValueError('Username already taken')
    else:
        inp_password1 = getpass('Enter password: ')
        inp_password2 = getpass('Enter password second time: ')

        if inp_password1.count(' ') >= 1:
            raise ValueError('Password cannot contain spaces')

        if len(inp_password1) == 0:
            raise ValueError('Password cannot be empty')

        if inp_password1 == inp_password2:
            with ConnectionHandler(**config) as ch:
                with CursorHandler(ch) as cursor:
                    query = 'INSERT INTO `users` (`id`, `username`, `password`) VALUES (NULL, %s, %s);'
                    cursor.execute(query, (inp_username, hashing_input(inp_password1)))
                    print('Registered')
        else:
            raise ValueError("Password's don't match")


def login():
    inp_username = input('Enter username: ')
    inp_password = getpass('Enter password: ')
    hashed_pas = hashing_input(inp_password)
    with ConnectionHandler(**config) as ch:
        with CursorHandler(ch) as cursor:
            query = 'SELECT count(*) FROM users WHERE username=%s AND password=%s'
            cursor.execute(query, (inp_username, hashed_pas))
            is_here, *_ = cursor
            if is_here[0]:
                print('Logged in')
                query = f"SELECT admin FROM users WHERE username='{inp_username}'"
                cursor.execute(query)
                is_admin, *_ = cursor
                user = User(inp_username, is_admin[0])
                user.main_menu()
            else:
                print('Wrong username or password')
                return


def list_error():
    print('Error: Please select from the list')


def main_menu():
    menu_dict = {
        '1': register,
        '2': login
    }
    inp = input('Select what you want to do:\n'
                '1 - register\n'
                '2 - login\n'
                '3 - shutdown\n')
    if inp == '3':
        return
    try:
        menu_dict.get(inp, list_error)()
    except ValueError as err:
        print('Error:', err)
    main_menu()


if __name__ == '__main__':
    main_menu()
