# main.py

import webapp2

# Later will change into Handler-Template
index = open('index.html', 'r')

class MainPage(webapp2.RequestHandler):
	def get(self):
		self.response.headers['Content-Type'] = 'text/html'
		self.response.write(index.readlines())

application = webapp2.WSGIApplication([('/', MainPage),], debug=True)
