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

providers = {
    'Google'   : 'https://www.google.com/accounts/o8/id',
    'Yahoo'    : 'yahoo.com',
    'MySpace'  : 'myspace.com',
    'AOL'      : 'aol.com',
    'MyOpenID' : 'myopenid.com'
    # add more here
}

authors = [('Chia-Hao Chen', 'https://github.com/chiahc1'), ('She Nie', 'https://github.com/nashn'), ('Greg Jeckell', 'http://www.gregjeckell.com/')]


class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)
    
    def render(self, template, template_values, **kw):
		t = JINJA_ENVIRONMENT.get_template(template)
		
		log_in = False
		sign_up = True
		
		user = users.get_current_user()
		if user:# signed in already
			log_in = True
			sign_up = False
			self.response.out.write('Hello <em>%s</em>! [<a href="%s">sign out</a>]' % (
				user.nickname(), users.create_logout_url(self.request.uri)))
		else:# let user choose authenticator
			self.response.out.write('Hello world! Sign in at: ')
			for name, uri in providers.items():
				self.response.out.write('[<a href="%s">%s</a>]' % (
					users.create_login_url(federated_identity=uri), name))

		course_list = db.GqlQuery("SELECT * FROM Course").fetch(1000)
		template_values = {'authors': authors,
					'course_list': course_list,
					'user' : user,
					'log_in': log_in,
					'sign_up': sign_up
			}

		self.write(t.render(template_values))


# this handler is just for test:
class BasePage(Handler):
	def get(self):
		self.render('base.html')

class MainPage(Handler):
	def get(self):
		#this is for data loading
		#dataloader.load()

		#course_list = db.GqlQuery("SELECT * FROM Course").fetch(1000)

		tvalues = {'authors': authors,
		#			'course_list': course_list
		}
		self.render('index.html', template_values=tvalues)

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


class LogoutPage(Handler):
	def get(self):
		MainPage.get()


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
#	This part needs to be modified, still working on this part 
#
####################################################################
####################################################################
class  CoursePage(Handler):
	def get(self, course_id):
		course_info = db.GqlQuery("SELECT * FROM Course WHERE course_id=%d" % int(course_id)).get()

		tvalues = {'authors': authors,
					'course_info': course_info
			}
		self.render('course.html', template_values=tvalues)
		

	def post(self):
		return 0

class LessonPage(Handler):
	def get(self, lesson_id):

		entries = db.GqlQuery("SELECT * FROM Entry WHERE lesson_id=%d" % int(lesson_id)).fetch(1000)
		tvalues = {'authors': authors,
					'entries' : entries
				}
		self.render('lesson.html', template_values=tvalues)
	
	def post(self):
		return 0

'''
####################################################################
class LessonEntry(Handler):
	def get(self):
		tvalues = {'authors': authors
				}
		self.render('entry.html', template_values=tvalues)
		
class Lesson1Page(Handler):
	def get(self):		
		entries = db.GqlQuery("SELECT * FROM ChineseLesson01").fetch(4)
		tvalues = {'authors': authors,
					'entry': entries
							}
		self.render('Lesson1CN.html', template_values=tvalues)

class ChinesePage(Handler):
	def get(self):
		tvalues = {'authors': authors
			}
		self.render('build.html', template_values=tvalues)
####################################################################
'''


class BuildCourse(Handler):
	def get(self):
		tvalues = {'authors': authors
			}
		self.render('buildCourse.html', template_values=tvalues)

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

		l = db.GqlQuery("SELECT * FROM Course WHERE course_id=%d" % c_id).get()
		s = "Success! Here is the entry:\n"
		s += "%s\n%s\n%s\n%s\n%s\n%s\n%s\n" % (l.course_id,
			l.course_title, l.author, 
			l.imgURL, l.course_description,
			l.source_language, l.destination_language)
		self.response.write(s)

class BuildLesson(Handler):
	def get(self):
		tvalues = {'authors': authors
			}
		self.render('buildLesson.html', template_values=tvalues)

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
		entry_lists = buildEntry(l_id=l_id,
									voca=vocabulary, 
									mean=meanings, 
									img=images, 
									src=src, 
									dest=dest, 
									note='this is for testing the entry note function')

		
		lesson = Lesson(course_id=c_id,
						lesson_id=l_id,
						lesson_title=l_title, 
						author=author,
						difficulty=difficulty,
						source_language=src,
						destination_language=dest,
						entries=entry_lists,
						questions=q,
						answers=a,
						notes=notes)
		lesson.put()

		l = db.GqlQuery("SELECT * FROM Lesson WHERE lesson_id=%d" % l_id).get()
		s = "Success! Here is the entry:\n"
		s += "%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s" % (l.course_id,
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
		self.response.write(s)


	def buildEntry(l_id, voca, means, img, src, dest, note):
		entry_id = []
		for i in range(0, len(voca)-1):
			entry_id.append(i)
			entry = Entry(entry_id = i,
						lesson_id = l_id,
						imgURLs = img[i],
						word = voca[i],
						mean = means[i],
						source_language = src,
						destination_language = dest,
						notes = note)
			entry.put()
		return entry_id