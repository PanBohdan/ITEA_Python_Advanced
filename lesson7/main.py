import hashlib
from getpass import getpass
from mysql_handler import ConnectionHandler, CursorHandler
from user import User
from constants import CONFIG


def hashing_input(inp):
    our_hash = hashlib.md5(inp.encode())
    return our_hash.hexdigest()


def register():
    inp_username = input('Enter username: ')
    if inp_username.count(' ') >= 1:
        raise ValueError('Username cannot contain spaces')
    elif len(inp_username) == 0:
        raise ValueError('Username cannot be empty')
    with ConnectionHandler(**CONFIG) as ch:
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
            with ConnectionHandler(**CONFIG) as ch:
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
    with ConnectionHandler(**CONFIG) as ch:
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
