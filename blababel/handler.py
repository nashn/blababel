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

class MainPage(webapp2.RequestHandler):

	def get(self):
		template = JINJA_ENVIRONMENT.get_template('index.html')
		#self.response.write('''<p>good till this part</p>''')
		self.response.write(template.render())


class TestPage(webapp2.RequestHandler):

	def get(self):
		teststring = 'Hello World!'
		template_values = {'teststring': teststring}
		template = JINJA_ENVIRONMENT.get_template('test.html')
		self.response.write(template.render(template_values))
