from google.appengine.ext import db
import webapp2
import os
from google.appengine.ext.webapp import template

class User(db.Model):
    username = db.StringProperty()
    passwd = db.StringProperty()

class RegisterPage(webapp2.RequestHandler):
    def get(self):
        template_values = {}
        path = os.path.join(os.path.dirname(__file__), 'register.html')
        self.response.out.write(template.render(path, template_values))
    
class AddUser(webapp2.RequestHandler):
    def post(self):
        user = User()
        user.username = self.request.get('username')
        user.passwd = self.request.get('passwd')
        user.put()
        self.redirect('http://localhost:8080')
class LoginPage(webapp2.RequestHandler):
    def get(self):
        template_values = {'login_status':'false', }
        path = os.path.join(os.path.dirname(__file__), 'login.html')
        self.response.out.write(template.render(path, template_values))
class Login(webapp2.RequestHandler):
    def post(self):
        username = self.request.get('username')
        passwd = self.request.get('passwd')
        q = db.GqlQuery("select * from User where username = :username and passwd = :passwd", username=username, passwd=passwd)
        count = q.count()
        if count == 1:
            login_status = 'true'
        else:
            login_status = 'false'
        template_values = {'login_status':login_status, }
        path = os.path.join(os.path.dirname(__file__), 'login.html')
        self.response.out.write(template.render(path, template_values))

app = webapp2.WSGIApplication([
                               ('/reg', RegisterPage),
                               ('/reg/add', AddUser),
                               ('/login', LoginPage),
                               ('/login/takelogin',Login),
                               ])


    
    


