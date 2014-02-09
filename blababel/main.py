# !/usr/python2.7
# main.py

import webapp2

from handler import *


handlers = [('/', MainPage),
			('/test', TestPage)
]

application = webapp2.WSGIApplication(handlers, debug=True)