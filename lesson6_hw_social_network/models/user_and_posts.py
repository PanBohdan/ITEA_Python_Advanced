from mongoengine import *
from datetime import datetime


class User(Document):
	username = StringField()
	password = StringField()
	date_of_registration = StringField()
	admin = BooleanField(default=False)
	super_admin = BooleanField(default=False)

	@classmethod
	def create_user(cls, username, password):
		now = datetime.now()
		date_string = now.strftime("%d/%m/%Y %H:%M:%S")
		User(username, password, date_of_registration=date_string).save()

	@classmethod
	def check_pass(cls, username, password):
		user = User.objects.filter(username=username).first()
		return user.password == password

	@classmethod
	def get_user_by_name(cls, username):
		return User.objects.filter(username=username).first()

	@classmethod
	def get_all_users(cls):
		return cls.objects

	def get_posts(self):
		return Post.objects.filter(user=self)


class Post(Document):
	user = ReferenceField(User)
	time = StringField()
	data = StringField()

	@classmethod
	def add_post(cls, user, data):
		now = datetime.now()
		date_string = now.strftime("%d/%m/%Y %H:%M:%S")
		Post(user, date_string, data).save()

	@classmethod
	def get_posts_by_user(cls, user):
		return cls.objects.filter(user=user)

	@classmethod
	def get_all_posts(cls):
		return cls.objects
