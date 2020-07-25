from index import db

class presenceservice(db.Model):

	__tablename__ = "user_regdetails"

	username = db.Column(db.String, primary_key=True)
	email= db.Column(db.String, nullable=False)
	password = db.Column(db.String, nullable=False)

	def __init__(self, username, email, password):
		self.username = username
		self.email = email
		self.password = password

	def __repr__(self):
		return '<{}>'.format(self.username, self.email)