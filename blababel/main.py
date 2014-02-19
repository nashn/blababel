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
			('/about', AboutPage),
			('/contact', ContactPage),
			# these are for later
			('/donation', DonationPage),
			('/error', ErrorPage),
			('/rank', RankPage),

			('/signup', SignupPage),
			('/login', LoginPage),
			('/logout', LogoutPage),
			(r'/game-([^/-]+)-([^/-]+)', GamePage),
			(r'/profile', ProfilePage),
			
			#the following is lessons, later
			(r'/course-([^/-]+)', CoursePage),
			(r'/course-([^/-]+)-lesson-([^/-]+)', LessonPage),
			
			('/buildLesson', BuildLesson),
			('/buildCourse', BuildCourse)
]

application = webapp2.WSGIApplication(handlers, debug=True)
