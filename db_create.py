from index import db
from models import presenceservice

db.create_all()

db.session.add(presenceservice("hi", "hlo@gmail.com", "hello"))

db.session.commit()