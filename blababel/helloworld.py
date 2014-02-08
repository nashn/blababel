import webapp2

form = """<input type='submit'> What is your birthday </input>"""

class MainPage(webapp2.RequestHandler):
	def get(self):
		self.response.headers['Content-Type'] = 'text/html'
		self.response.write(form)


application = webapp2.WSGIApplication([('/', MainPage),], debug=True)
