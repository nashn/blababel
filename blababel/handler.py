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
HEADER_TEMPLATE = JINJA_ENVIRONMENT.get_template('template/header.html')
NAVIGATION_TEMPLATE = JINJA_ENVIRONMENT.get_template('template/navigation.html')
FOOTER_TEMPLATE = JINJA_ENVIRONMENT.get_template('template/footer.html')

def build_page(self, htmlFile, params={}):
		page = JINJA_ENVIRONMENT.get_template(htmlFile)
		self.response.write(HEADER_TEMPLATE.render())
		self.response.write(NAVIGATION_TEMPLATE.render())
		self.response.write(page.render(params))
		self.response.write(FOOTER_TEMPLATE.render())

class MainPage(webapp2.RequestHandler):

	def get(self):
		build_page(self, 'index.html')

	def post(self):
		firstname = self.request.get('firstname')
		lastname = self.request.get('lastname')
		email = self.request.get('email')
		password = self.request.get('password')
		sex = self.request.get('sex')
		params = {'firstname':firstname, 'lastname':lastname, 'email':email, 'password':password, 'sex':sex}
		build_page(self, 'test.html', params)

class TestPage(webapp2.RequestHandler):

	def get(self):
		teststring = 'Hello World!'
		template_values = {'teststring': teststring}
		template = JINJA_ENVIRONMENT.get_template('test.html')
		self.response.write(template.render(template_values))
