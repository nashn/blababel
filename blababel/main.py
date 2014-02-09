# !/usr/python2.7
# main.py
'''
If adding a new page, need to add a new tuple into the handlers list 
'''
import webapp2
from handler import *


handlers = [('/base', BasePage),
			('/', MainPage),
			('/building', BuildPage),
			('/error', ErrorPage),
			('/rank', RankPage),
			('/about', AboutPage),
			('/donation', DonationPage),
			#the following is lessons, later
			('/lessons', LessonPage),
			('/chinese', ChinesePage)
]

application = webapp2.WSGIApplication(handlers, debug=True)
