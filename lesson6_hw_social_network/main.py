from login_and_register import login, register
from mongoengine import *
from models.user_and_posts import User, Post
connect('social_network')


class UserMenu:
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
        dict_of_actions = {
            '1': self.add_post,
            '2': self.see_posts,
            '3': self.user_posts,
            '4': self.list_of_users,
            '5': self.add_admin
        }
        if not inp == '6':
            dict_of_actions.get(inp, list_error)()
            self.super_admin_menu()
        else:
            return

    def admin_menu(self):
        inp = input('\n'
                    'Admin menu\n'
                    'Select what you want to do:\n'
                    '1 - add post\n'
                    '2 - see posts\n'
                    '3 - select user posts and register date\n'
                    '4 - list of users and do they have admin rights\n'
                    '5 - logout\n')
        dict_of_actions = {
            '1': self.add_post,
            '2': self.see_posts,
            '3': self.user_posts,
            '4': self.list_of_users,
        }
        if not inp == '5':
            dict_of_actions.get(inp, list_error)()
            self.admin_menu()
        else:
            return

    def user_menu(self):
        inp = input('\n'
                    'User menu\n'
                    'Select what you want to do:\n'
                    '1 - add post\n'
                    '2 - see posts\n'
                    '3 - logout\n')
        dict_of_actions = {
            '1': self.add_post,
            '2': self.see_posts,
        }
        if not inp == '3':
            dict_of_actions.get(inp, list_error)()
            self.user_menu()
        else:
            return

    def add_post(self):
        inp = input('Enter what you want to write:\n')
        Post.add_post(User.get_user_by_name(self._username), inp)

    @staticmethod
    def see_posts():
        all_posts = Post.get_all_posts()
        for post in all_posts:
            print(f"{post.time} {post.user.username}:{post.data}")

    @staticmethod
    def user_posts():
        inner_inp = input('Enter the user you want to find:\n')
        us = User.get_user_by_name(inner_inp)
        print(f"User {us.username} was registered at {us.date_of_registration}\n"
              f"his posts:")
        posts = Post.get_posts_by_user(us)
        for post in posts:
            print(f"{post.time} {post.user.username}:{post.data}")

    @staticmethod
    def list_of_users():
        users = User.get_all_users()
        for user in users:
            print(f"{user.username}, admin:{user.admin} super_admin:{user.super_admin}")

    @staticmethod
    def add_admin():
        inp = input('Enter name of user you want to make an admin')
        us = User.get_user_by_name(inp)
        us.admin = True
        us.save()


def list_error():
    print('Error: Please select from the list')


def main_menu():

    inp = input('Select what you want to do:\n'
                '1 - register\n'
                '2 - login\n'
                '3 - shutdown\n')
    try:
        if inp == '1':
            register()
        elif inp == '2':
            local_login, logged_in = login()
            if logged_in:
                us = User.get_user_by_name(local_login)
                user_menu = UserMenu(us.username, us.admin, us.super_admin)
                user_menu.main_menu()
            else:
                raise ValueError('Wrong username or password')
        elif inp == '3':
            return
    except ValueError as err:
        print('Error:', err)
    main_menu()


if __name__ == '__main__':
    main_menu()
