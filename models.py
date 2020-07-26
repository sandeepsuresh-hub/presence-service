from index import db
from werkzeug.security import check_password_hash, generate_password_hash

class presenceservice(db.Model):

	__tablename__ = "user_regdetails"

	username = db.Column(db.String, primary_key=True)
	email= db.Column(db.String, nullable=False)
	password = db.Column(db.String, nullable=False)

	def __init__(self, username, email, password):
		self.username = username
		self.email = email
		self.password = password

	def set_password(self, password):
		self.password = generate_password_hash(
			password,
			method='sha256' )


	def check_password(self,password):
		return check_password_hash(self.password, password)

	def __repr__(self):
		return '<{}>'.format(self.username, self.email)