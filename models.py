from google.appengine.ext import db
import webapp2
import os
from google.appengine.ext.webapp import template

class User(db.Model):
    username = db.StringProperty()
    passwd = db.StringProperty()

class Register(webapp2.RequestHandler):
    def get(self):
        template_values={}
        path = os.path.join(os.path.dirname(__file__),'register.html')
        self.response.out.write(template.render(path,template_values))
    
class AddUser(webapp2.RequestHandler):
    def post(self):
        user = User()
        user.username = self.request.get('username')
        user.passwd = self.request.get('passwd')
        user.put()
        self.redirect('http://localhost:8080')

app = webapp2.WSGIApplication([
                               ('/reg',Register),
                               ('/reg/add',AddUser)
                               ])


    
    


