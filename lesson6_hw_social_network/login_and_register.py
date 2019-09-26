from getpass import getpass
from models.user_and_posts import User
import hashlib


def hashing_input(inp):
    our_hash = hashlib.md5(inp.encode())
    return our_hash.hexdigest()


def register():
    inp_username = input('Enter username: ')
    if inp_username.count(' ') >= 1:
        raise ValueError('Username cannot contain spaces')

    if len(inp_username) == 0:
        raise ValueError('Username cannot be empty')

    if User.get_user_by_name(inp_username):
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
            User.create_user(inp_username, hashed_pas)
        else:
            raise ValueError("Password's don't match")


def login():
    inp_username = input('Enter username: ')
    inp_password = getpass('Enter password: ')
    hashed_pas = hashing_input(inp_password)
    if User.check_pass(inp_username, hashed_pas):
        print('Login successful')
        return inp_username, True
    else:
        print('Login failed')
        return inp_username, False
