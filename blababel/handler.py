# !/usr/python2.7
# handler.py

'''
Adding a new page with a new handlers
Maybe change to generic handler class later
'''
import os
import webapp2
import jinja2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True
    )

authors = ['Chia-Hao Chen', 'She Nie', 'Greg Jeckell']

class BasePage(webapp2.RequestHandler):

	def get(self):
		template_values = {'authors': authors
						}
		template = JINJA_ENVIRONMENT.get_template('base.html')
		self.response.write(template.render(template_values))

class MainPage(webapp2.RequestHandler):
	def get(self):
		template_values = {'authors': authors
						}
		template = JINJA_ENVIRONMENT.get_template('index.html')
		self.response.write(template.render(template_values))

	def post(self):
		firstname = self.request.get('firstname')
		lastname = self.request.get('lastname')
		email = self.request.get('email')
		password = self.request.get('password')
		sex = self.request.get('sex')
		params = {'firstname':firstname, 'lastname':lastname, 
              'email':email, 'password':password, 'sex':sex}
		self.response.write(params) #TODO handle the post request just demonstrating for now

class BuildPage(webapp2.RequestHandler):

	def get(self):
		teststring = 'Hello World!'
		template_values = {'authors': authors,
						'teststring': teststring
						}
		template = JINJA_ENVIRONMENT.get_template('build.html')
		self.response.write(template.render(template_values))

class ChinesePage(webapp2.RequestHandler):

	def get(self):
		template_values = {'authors': authors,
						}
		template = JINJA_ENVIRONMENT.get_template('chinese.html')
		self.response.write(template.render(template_values))
