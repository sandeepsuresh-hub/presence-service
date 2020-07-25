from flask import Flask, render_template, g, redirect, url_for, request, session, flash
from forms import LoginForm, RegisterForm
#from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
#import sqlite3 

app = Flask(__name__)

app.secret_key = 'my application'
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///presenceservice.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False

db = SQLAlchemy(app)

from models import *

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/home")
def home():
    presenceservices = db.session.query(presenceservice).all()
    return render_template("home.html", presenceservice=presenceservice)

@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	form = LoginForm(request.form)
	if request.method == 'POST':
		if form.validate_on_submit():
			if request.form['username'] != 'admin' or request.form['password'] != 'admin':
				error = 'Invalid credentials. Please try again!!!'
			else:
				session['logged in'] = True
				flash('You just logged in!')
				return redirect(url_for('home'))
	return render_template('login.html', form=form, error=error)

@app.route("/logout")
def logout():
	session.pop('logged in', None)
	flash('You just logged out!')
	return redirect(url_for('login'))

@app.route("/register", methods=['GET', 'POST'])
def register():	
	form = RegisterForm()
	if form.validate_on_submit():
		user = User(
			username=form.username.data,
			email=form.email.data,
			password=form.password.data)
		db.session.add(user)
		db.session.commit()
		login_user(user)
		return redirect(url_for('home'))
	return render_template('register.html', form=form)

#def connect_db():
	#return sqlite3.connect(app.database)

if __name__ == '__main__':
	app.run(debug=True)