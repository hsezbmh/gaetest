import datetime
from google.appengine.ext import db

class User(db.Model):
    username = db.StringProperty()
    passwd = db.StringProperty()
    createdate = db.DateProperty()