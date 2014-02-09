# !/usr/python2.7
# main.py
'''
If adding a new page, need to add a new tuple into the handlers list 
'''
import webapp2

from handler import *


handlers = [('/', MainPage),
			('/test', TestPage)
]

application = webapp2.WSGIApplication(handlers, debug=True)