# !/usr/python2.7
# handler.py

'''
Adding a new page with a new handlers
Maybe change to generic handler class later
'''
import os
import webapp2
import jinja2
from google.appengine.ext import db

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True
    )

authors = ['Chia-Hao Chen', 'She Nie', 'Greg Jeckell']

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)
    def render_str(self, template, **params):
        t = JINJA_ENVIRONMENT.get_template(template)
        return t.render(params)
    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

class BasePage(Handler):
	def get(self):
		self.render('base.html')

class MainPage(Handler):
	def get(self):
		self.render('index.html')

	def post(self):
		firstname = self.request.get('firstname')
		lastname = self.request.get('lastname')
		email = self.request.get('email')
		password = self.request.get('password')
		sex = self.request.get('sex')
		params = {'firstname':firstname, 'lastname':lastname, 
              'email':email, 'password':password, 'sex':sex}
		self.response.write(params) #TODO handle the post request just demonstrating for now

class BuildPage(Handler):
	def get(self):
		s = 'Hello World!'
		self.render('build.html', teststring=s)

class ChinesePage(Handler):
	def get(self):
		self.render('chinese.html', authors=['Chia-Hao Chen', 'She Nie', 'Greg Jeckell'])
