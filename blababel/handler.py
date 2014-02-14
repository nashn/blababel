# !/usr/python2.7
# handler.py

import os
import webapp2
import jinja2

from classes.ObjectProperty import ObjectProperty
from google.appengine.api import users
from google.appengine.ext import db

from google.appengine.ext.webapp.util import run_wsgi_app

from schema import *
#this is for data loading
#import dataloader

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True
    )

providers = [('Google', 'https://www.google.com/accounts/o8/id'),
			('Yahoo', 'yahoo.com')
    # add more here
]

authors = [('Chia-Hao Chen', 'https://github.com/chiahc1'), 
			('She Nie', 'https://github.com/nashn'), 
			('Greg Jeckell', 'http://www.gregjeckell.com/')
]


class Handler(webapp2.RequestHandler):
	
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)
    
    def render(self, template, template_values, **kw):
		t = JINJA_ENVIRONMENT.get_template(template)
		
		log_in = False
		sign_up = True
		
		user = users.get_current_user()
		login = [('/', 'BlaBabel')]
		logout = users.create_logout_url(self.request.uri)
		uProfile = None
		
		if user:# signed in already
			log_in = True
			sign_up = False

			uProfile = db.GqlQuery("SELECT * FROM UserProfile WHERE uid=1").get()
			if not uProfile:
				u = UserProfile(uid=1, username=user.nickname(), courses=[0,1], scores=[('lesson1',100)])
				u.put()
			uProfile = db.GqlQuery("SELECT * FROM UserProfile WHERE uid=1").get()
			
			#self.response.out.write('Hello <em>%s</em>! [<a href="%s">sign out</a>]' % (
			#	user.nickname(), users.create_logout_url(self.request.uri)))
		if not user:# let user choose authenticator
			for name, uri in providers:
				login.append(tuple([users.create_login_url(federated_identity=uri), name]))

		course_list = db.GqlQuery("SELECT * FROM Course").fetch(1000)

		# add new attritube to the dictionary
		template_values['authors'] = authors
		template_values['course_list'] = course_list
		template_values['user'] = user
		template_values['log_in'] = log_in
		template_values['sign_up'] = sign_up
		template_values['login'] = login
		template_values['logout'] = logout
		template_values['uProfile'] = uProfile
		
		self.write(t.render(template_values))


# this handler is just for test:
class BasePage(webapp2.RequestHandler):
	def baseRender(self, template, template_values):
		t = JINJA_ENVIRONMENT.get_template(template)
		self.write(t.render(template_values))

class MainPage(Handler):
	def get(self):
		#this is for data loading
		#dataloader.load()

		self.render('index.html', template_values={})

	def post(self):
		f = self.request.get('firstname')
		l = self.request.get('lastname')
		e = self.request.get('email')
		p = self.request.get('password')
		pp = self.request.get('passwordRe')
		user = User(firstname=f, lastname=l, email=e, password=p)
		user.put()
		newUser = db.GqlQuery("SELECT * FROM User").get()
		self.response.write(newUser[0].firstname)


'''
class LogoutPage(Handler):
	def get(self):
		user = users.get_current_user()
		if user:# signed in already
			log_in = True
			sign_up = False
			self.response.out.write('Hello <em>%s</em>! [<a href="%s">sign out</a>]' % (
				user.nickname(), users.create_logout_url(self.request.uri)))
		self.render('index.html', template_values={})
'''

#########################################################################
# The following are static handlers
#########################################################################
class BuildPage(Handler):
	def get(self):
		tvalues = {'authors': authors,
					'teststring' : 'Hello World'
					}
		self.render('build.html', template_values=tvalues)

class RankPage(Handler):
	def get(self):
		tvalues = {'authors': authors,
					'teststring' : 'Hello World'
					}
		self.render('rank.html', template_values=tvalues)
	
	def post(self):
		return 0

class AboutPage(Handler):
	def get(self):
		tvalues = {'authors': authors,
					'teststring' : 'Hello World'
					}
		self.render('about.html', template_values=tvalues)

class DonationPage(Handler):
	def get(self):
		tvalues = {'authors': authors,
					'teststring' : 'Hello World'
					}
		self.render('donation.html', template_values=tvalues)

	def post(self):
		return 0

class GamePage(Handler):
	def get(self):
		tvalues = {'authors': authors,
					'teststring' : 'Hello World'
					}
		self.render('game.html', template_values=tvalues)

	def post(self):
		return 0

# TODO: implement error handler
class ErrorPage(Handler):
	def get(self):
		tvalues = {'authors': authors,
					'teststring' : 'Hello World'
					}
		self.render('404.html', template_values=tvalues)


class ProfilePage(Handler):
	def get(self):
		tvalues = {'authors': authors,
					'teststring' : 'Hello World'
					}
		self.render('profile.html', template_values=tvalues)
	def post(self):
		return 0

####################################################################
####################################################################
#
#	The following part is for showing courses and lessons
#
####################################################################
####################################################################
class  CoursePage(Handler):
	def get(self, course_id):
		course_info = db.GqlQuery("SELECT * FROM Course WHERE course_id=%d" % int(course_id)).get()
		self.render('course.html', template_values={'course_info' : course_info})
		

	def post(self):
		return 0

class LessonPage(Handler):
	def get(self, lesson_id):
		entries = db.GqlQuery("SELECT * FROM Entry WHERE lesson_id=%d" % int(lesson_id)).fetch(1000)
		self.render('lesson.html', template_values={'entries' : entries})
	
	def post(self):
		return 0


####################################################################
####################################################################
#
#	The following part is for adding courses and lessons
#
####################################################################
####################################################################

class BuildCourse(Handler):
	def get(self):
		self.render('buildCourse.html', template_values={})

	def post(self):
		c_id = int(self.request.get('course_id'))
		c_title = self.request.get('course_title')
		author = self.request.get('author')
		c_img = self.request.get('course_img')
		desc = self.request.get('desc')
		src = self.request.get('src')
		dest = self.request.get('dest')
		
		course = Course(course_id=c_id, 
						course_title=c_title, 
						author=author, 
						source_language=src, 
						destination_language=dest,
						imgURL=c_img, 
						course_description=desc, 
						lessons=[1,2,3,4,5])
		course.put()

		print 'good till this point'

		l = db.GqlQuery("SELECT * FROM Course WHERE course_id=%d" % c_id).get()
		s = "Success! Here is the entry:\n"
		s += "%s\n%s\n%s\n%s\n%s\n%s\n%s\n" % (l.course_id,
			l.course_title,
			l.author, 
			l.imgURL, 
			l.course_description,
			l.source_language, 
			l.destination_language)
		self.response.render('base.html', template_values={'result' : s})

class BuildLesson(Handler):
	def get(self):
		self.render('buildLesson.html', template_values={})

	def post(self):
		c_id = int(self.request.get('course_id'))
		l_id = int(self.request.get('lesson_id'))
		l_title = self.request.get('lesson_title')
		difficulty = self.request.get('diff')
		author = self.request.get('author')
		
		vocabulary = self.request.get('words').split(',')
		meanings = self.request.get('meanings').split(',')
		q = []
		a = []
		for i in range(0,3):
			q.append(self.request.get("q%s" % i))
			a.append(self.request.get("a%s" % i))
		images = self.request.get('imgs').split(',')
		notes = self.request.get('notes')
		src = self.request.get('src')
		dest = self.request.get('dest')


		# helper function for creating entries:
		entry_ids = []
		for i in range(0, len(vocabulary)-1):
			entry_ids.append(i)
			entry = Entry(entry_id = i,
						lesson_id = l_id,
						imgURLs = img[i],
						word = vocabulary[i],
						mean = meanings[i],
						source_language = src,
						destination_language = dest,
						notes = notes)
			entry.put()


		lesson = Lesson(course_id=c_id,
						lesson_id=l_id,
						lesson_title=l_title, 
						author=author,
						difficulty=difficulty,
						source_language=src,
						destination_language=dest,
						entries=entry_ids,
						questions=q,
						answers=a,
						notes=notes)
		lesson.put()


		l = db.GqlQuery("SELECT * FROM Lesson WHERE lesson_id=%d" % l_id).get()
		s = "Success! Here is the entry:\n"
		s += "%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n" % (l.course_id,
			l.lesson_id, 
			l.lesson_title, 
			l.author, 
			l.difficulty, 
			l.source_language, 
			l.destination_language,
			l.entries,
			l.questions, 
			l.answers,
			l.notes)

		self.render('base.html', template_values={'result' : s})