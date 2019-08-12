import shelve
from getpass import getpass
import hashlib
from datetime import datetime
import os.path


db_name = 'user_data.db'
admin_db_name = 'admin_rights.db'
posts_db_name = 'posts_and_users.db'
post_key = 'list_of_posts'
users_key = 'list_of_users'


class User:
    def __init__(self, username, admin, super_admin):
        self._username = username
        self._admin = admin
        self._super_admin = super_admin

    def main_menu(self):
        if self._admin:
            if self._super_admin:
                self.super_admin_menu()
            else:
                self.admin_menu()
        else:
            self.user_menu()

    def super_admin_menu(self):
        inp = input('\n'
                    'Super admin menu\n'
                    'Select what you want to do:\n'
                    '1 - add post\n'
                    '2 - see posts\n'
                    '3 - select user posts and register date\n'
                    '4 - list of users and do they have admin rights\n'
                    '5 - add admin\n'
                    '6 - logout\n')

        if inp == '1':
            inp = input('Enter what you want to write:\n')
            now = datetime.now()
            date_string = now.strftime("%d/%m/%Y %H:%M:%S")
            with shelve.open(posts_db_name) as db:
                general_posts = db.get(post_key)
                general_posts.append((self._username, date_string, inp))
                db.update({post_key: general_posts})
                date, post_list = db.get(self._username)
                post_list.append((self._username, date_string, inp))
                db.update({self._username: (date, post_list)})

        if inp == '2':
            with shelve.open(posts_db_name) as db:
                our_list = db.get(post_key)
                for x in our_list:
                    print(x)

        if inp == '3':
            with shelve.open(posts_db_name) as db:
                inner_inp = input('Enter the user you want to find:\n')
                try:
                    date_of_registration, posts = db.get(inner_inp)
                    print(f"User {inner_inp} was registered at {date_of_registration}\n"
                          f"his posts: {posts}")
                except TypeError:
                    print('There is no data on that user in database now')

        if inp == '4':
            with shelve.open(posts_db_name) as db:
                output = list(db.keys())
                output.remove(post_key)
                for x in output:
                    with shelve.open(admin_db_name) as admin:
                        admin_rights = admin.get(x, False)
                    print(f"{x}, admin: {admin_rights[0]} super_admin: {admin_rights[1]}")

        if inp == '5':
            inp = input('Enter name of user you want to make an admin')
            add_admin(inp, True, False)

        if inp == '6':
            return
        else:
            list_error()
        self.super_admin_menu()

    def admin_menu(self):
        inp = input('\n'
                    'Admin menu\n'
                    'Select what you want to do:\n'
                    '1 - add post\n'
                    '2 - see posts\n'
                    '3 - select user posts and register date\n'
                    '4 - list of users and do they have admin rights\n'
                    '5 - logout\n')

        if inp == '1':
            inp = input('Enter what you want to write:\n')
            now = datetime.now()
            date_string = now.strftime("%d/%m/%Y %H:%M:%S")
            with shelve.open(posts_db_name) as db:
                general_posts = db.get(post_key)
                general_posts.append((self._username, date_string, inp))
                db.update({post_key: general_posts})
                date, post_list = db.get(self._username)
                post_list.append((self._username, date_string, inp))
                db.update({self._username: (date, post_list)})

        if inp == '2':
            with shelve.open(posts_db_name) as db:
                our_list = db.get(post_key)
                for x in our_list:
                    print(x)

        if inp == '3':
            with shelve.open(posts_db_name) as db:
                inner_inp = input('Enter the user you want to find:\n')
                try:
                    date_of_registration, posts = db.get(inner_inp)
                    print(f"User {inner_inp} was registered at {date_of_registration}\n"
                          f"his posts: {posts}")
                except TypeError:
                    print('There is no data on that user in database now')

        if inp == '4':
            with shelve.open(posts_db_name) as db:
                output = list(db.keys())
                output.remove(post_key)
                for x in output:
                    with shelve.open(admin_db_name) as admin:
                        admin_rights = admin.get(x, False)
                    print(f"{x}, admin: {admin_rights[0]} super_admin: {admin_rights[1]}")

        if inp == '5':
            return
        else:
            list_error()
        self.admin_menu()

    def user_menu(self):
        inp = input('\n'
                    'User menu\n'
                    'Select what you want to do:\n'
                    '1 - add post\n'
                    '2 - see posts\n'
                    '3 - logout\n')
        if inp == '1':
            inp = input('Enter what you want to write:\n')
            now = datetime.now()
            date_string = now.strftime("%d/%m/%Y %H:%M:%S")
            with shelve.open(posts_db_name) as db:
                general_posts = db.get(post_key)
                general_posts.append((self._username, date_string, inp))
                db.update({post_key: general_posts})
                date, post_list = db.get(self._username)
                post_list.append((self._username, date_string, inp))
                db.update({self._username: (date, post_list)})

        if inp == '2':
            with shelve.open(posts_db_name) as db:
                for x in db.get(post_key):
                    print(x)

        if inp == '3':
            return
        else:
            list_error()
        self.user_menu()


def hashing_input(inp):
    our_hash = hashlib.md5(inp.encode())
    return our_hash.hexdigest()


def register():
    inp_username = input('Enter username: ')
    with shelve.open(db_name) as db:
        if inp_username.count(' ') >= 1:
            raise ValueError('Username cannot contain spaces')

        if len(inp_username) == 0:
            raise ValueError('Username cannot be empty')

        if db.get(inp_username):
            raise ValueError('Username already taken')

        else:
            inp_password1 = getpass('Enter password: ')
            inp_password2 = getpass('Enter password second time: ')

            if inp_password1.count(' ') >= 1:
                raise ValueError('Password cannot contain spaces')

            if len(inp_password1) == 0:
                raise ValueError('Password cannot be empty')

            if inp_password1 == inp_password2:
                hashed_pas = hashing_input(inp_password1)
                db.update({inp_username: hashed_pas})
                now = datetime.now()
                date_string = now.strftime("%d/%m/%Y %H:%M:%S")
                with shelve.open(posts_db_name) as in_db:
                    in_db.update({inp_username: (date_string, [])})
            else:
                raise ValueError("Password's don't match")


def login():
    inp_username = input('Enter username: ')
    inp_password = getpass('Enter password: ')
    hashed_pas = hashing_input(inp_password)
    with shelve.open(db_name) as db:
        if db.get(inp_username) == hashed_pas:
            print('Login successful')
            with shelve.open(admin_db_name) as admin:
                admin_rights, super_admin_rights = admin.get(inp_username, (False, False))
                user = User(inp_username, admin_rights, super_admin_rights)
            user.main_menu()
        else:
            print('Login failed')


def add_admin(name, admin, super_admin):
    with shelve.open(admin_db_name) as db:
        db.update({name: (admin, super_admin)})


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


def create_posts_and_users():
    with shelve.open(posts_db_name) as db:
        db[post_key] = []


if __name__ == '__main__':
    if not os.path.exists('posts_and_users.db'):
        create_posts_and_users()
    main_menu()
