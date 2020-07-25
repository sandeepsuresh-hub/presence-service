from index import db
from models import presenceservice

db.create_all()

db.session.add(presenceservice("hi", "hlo", "hello"))

db.session.commit()