from flask import Flask, render_template, g, redirect, url_for, request, session, flash
from form import LoginForm, RegisterForm
from flask_login import login_user, login_required, logout_user
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)

app.secret_key = 'my application'
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///presenceservice.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False

db = SQLAlchemy(app)

from models import *


@app.route("/")
def index():
    return render_template("index.html")

def set_password(self, password):
	self.password = generate_password_hash(
	password,
	method='sha256' )


def check_password(self,password):
	return check_password_hash(self.password, password)

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
			user = presenceservice.query.filter_by(username=form.username.data).first()
			password = presenceservice.query.filter_by(password=form.password.data).first()
			if user and password:
				session['logged in'] = True
				flash('You just logged in!')
				return redirect(url_for('home'))
		else:
			error = 'Invalid credentials. Please try again!!!'
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
		existing_user = presenceservice.query.filter_by(username=form.username.data).first()
		if existing_user is None:
			user = presenceservice(
				username=form.username.data,
				email=form.email.data,
				password=form.password.data)
			db.session.add(user)
			db.session.commit()
			flash('Registered Successfully!')
			return redirect(url_for('home'))
	return render_template('register.html', form=form)

if __name__ == '__main__':
	app.run(debug=True)