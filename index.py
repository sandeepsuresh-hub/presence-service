from flask import Flask, render_template, redirect, url_for, request, session, flash
#from functools import wraps

app = Flask(__name__)

app.secret_key = 'my application'

def login_required(f):
	@wraps(f)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			returnf(*args, **kwargs)
		else:
			flash('You need to login first!')
			return redirect(url_for('login'))
	return wrap

@app.route("/")
#@login_required
def home():
    return render_template("home.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] != 'admin' or request.form['password'] != 'admin':
			error = 'Invalid credentials. Please try again!!!'
		else:
			session['logged in'] = True
			flash('You just logged in!')
			return redirect(url_for('dashboard'))
	return render_template('login.html', error=error)

@app.route("/logout")
#@login_required
def logout():
	session.pop('logged in', None)
	flash('You just logged out!')
	return redirect(url_for('login'))

if __name__ == '__main__':
	app.run(debug=True)