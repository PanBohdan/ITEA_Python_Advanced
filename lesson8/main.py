from flask import Flask, redirect, render_template, request, session, abort
import os
from mysql_handler import ConnectionHandler, CursorHandler
from werkzeug.exceptions import BadRequestKeyError

app = Flask(__name__)
config = {
	'user': 'root',
	'password': 'ThatSomeStrongPassword',
	'host': 'localhost',
	'database': 'shop_db',
	'raise_on_warnings': True
}


@app.route('/')
def main_page():
	with ConnectionHandler(**config) as ch:
		with CursorHandler(ch) as cursor:
			query = 'SELECT * FROM `categories`'
			cursor.execute(query)
			our_list = []
			for c_id, name, info in cursor:
				our_list.append([c_id, name, info])
	return render_template('main_page.html', items=our_list)


@app.route('/info')
def info_page():
	return render_template('info.html')


@app.route('/admin')
def admin_page():
	with ConnectionHandler(**config) as ch:
		with CursorHandler(ch) as cursor:
			query = 'SELECT * FROM `categories`'
			cursor.execute(query)
			our_list = []
			for c_id, name, info in cursor:
				our_list.append([c_id, name, info])
	return render_template('admin_page.html', popup='', items=our_list)


@app.route('/add_category', methods=['POST', 'GET'])
def admin_category():
	with ConnectionHandler(**config) as ch:
		with CursorHandler(ch) as cursor:
			query = 'SELECT * FROM `categories`'
			cursor.execute(query)
			our_list = []
			for c_id, name, info in cursor:
				our_list.append([c_id, name, info])
	if request.method == 'POST' and request.form:
		name = request.form['name']
		print(request.form)
		if name:
			description = request.form['description']
			print(name, description)
			with ConnectionHandler(**config) as ch:
				with CursorHandler(ch) as cursor:
					query = f'INSERT INTO `categories` (`id`, `name`, `info`) VALUES (NULL, %s, %s)'
					cursor.execute(query, (name, description))
			return render_template('admin_page.html', popup='done', items=our_list)
		else:
			return render_template('admin_page.html', popup='Error: name must be entered', items=our_list)
	else:
		return 'none'


@app.route('/add_item', methods=['POST', 'GET'])
def admin_item():
	with ConnectionHandler(**config) as ch:
		with CursorHandler(ch) as cursor:
			query = 'SELECT * FROM `categories`'
			cursor.execute(query)
			our_list = []
			for c_id, name, info in cursor:
				our_list.append([c_id, name, info])
	if request.method == 'POST' and request.form:
		if request.form['name']:
			try:
				name = request.form['name']
				category_id = request.form['options']
				price = request.form['price']
				in_stock = request.form['in_stock']
				number_of_items = request.form['number_of_items']
				with ConnectionHandler(**config) as ch:
					with CursorHandler(ch) as cursor:
						query = "INSERT INTO `storage` " \
								"(`id`, `name`, `category`, `price`, `in_stock`, `number_of_items`)" \
								" VALUES (NULL, %s, %s, %s, %s, %s)"
						if in_stock == 'on':
							in_stock = 1
						else:
							in_stock = 0
						cursor.execute(query, (name, category_id, price, in_stock, number_of_items))
						return render_template('admin_page.html', popup='done', items=our_list)
			except BadRequestKeyError:
				return render_template('admin_page.html', popup='Error: please select category', items=our_list)
		else:
			return render_template('admin_page.html', popup='Error: name must be entered', items=our_list)
	else:
		return 'none'


@app.route("/<string:db>")
def find_in_db(db):
	with ConnectionHandler(**config) as ch:
		with CursorHandler(ch) as cursor:
			query = f'SELECT * FROM `storage` WHERE category={db}'
			cursor.execute(query)
			our_list = []
			for _, name, category, price, in_stock, number_of_items in cursor:
				if in_stock:
					in_stock = 'Yes'
				else:
					in_stock = 'No'
				our_list.append([name, category, price, in_stock, number_of_items])
		with ConnectionHandler(**config) as ch1:
			with CursorHandler(ch1) as cursor:
				query = f'SELECT * FROM `categories` WHERE id={db}'
				cursor.execute(query)
				for c_id, name, _ in cursor:
					for item in our_list:
						item[1] = name
		return render_template('storage.html', items=our_list)


if __name__ == "__main__":
	app.secret_key = os.urandom(12)
	app.run(debug=True, host='0.0.0.0', port=4000)
