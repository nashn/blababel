# !/usr/python2.7
# handler.py

import os
import webapp2
import jinja2
from classes.ObjectProperty import ObjectProperty
from google.appengine.ext import db

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True
    )

authors = ['Chia-Hao Chen', 'She Nie', 'Greg Jeckell']

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)
    
    def render(self, template, template_values):
    	t = JINJA_ENVIRONMENT.get_template(template)
        self.write(t.render(template_values))

class BasePage(Handler):
	def get(self):
		self.render('base.html')

class MainPage(Handler):
	def get(self):
		tvalues = {'authors': authors
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
		newUser = db.GqlQuery("SELECT * FROM User").fetch(10)
		self.response.write(newUser[0].firstname)

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

class LessonPage(Handler):
	def get(self):
		tvalues = {'authors': authors,
					'entry' : entry
				}
		self.render('lesson.html', template_values=tvalues)
	
	def post(self):
		return 0

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
		self.render('chinese.html', template_values=tvalues)

class BuildLesson(Handler):
	def get(self):
		tvalues = {'authors': authors
			}
		self.render('buildLesson.html', template_values=tvalues)

	def post(self):
		l_id = int(self.request.get('lesson_id'))
		l_title = self.request.get('lesson_title')
		author = self.request.get('author')
		vocabulary = self.request.get('v').split()
		images = self.request.get('imgs').split()
		q = []
		a = []
		for i in range(0,3):
			q.append(self.request.get("q%s" % i))
			a.append(self.request.get("a%s" % i))
		notes = self.request.get('notes')
		src = self.request.get('src')
		dest = self.request.get('dest')
		
		lesson = Lesson(lesson_id=l_id, lesson_title=l_title, author=author,
			vocabulary=vocabulary, imgURLs=images, questions=q, answers=a,
			notes=notes, source_language=src, destination_language=dest)
		lesson.put()

		lessons = db.GqlQuery("SELECT * FROM Lesson WHERE lesson_id=001").fetch(10)
		s = ""
		for entity in lessons:
			s += "%s: %s" % (lesson.lesson_id, lesson.answers)
		self.response.write(s)

###########################################
#
# The following code maybe seperated into an independent database file
#
###########################################
class User(db.Model):
	firstname = db.StringProperty(required = True)
	lastname = db.StringProperty(required = True)
	email = db.StringProperty(required = True)
	password = db.StringProperty(required = True)

class Offer(db.Model):
	course_id = db.IntegerProperty(required=True)
	creater = db.StringProperty(required = True)
	language = db.StringProperty(required = True)
	lesson_id = db.IntegerProperty(required = True)
	imageULR = db.StringProperty(required = True)
	desc = db.StringProperty()
'''	
class ChineseOffer(course_id, creater, language, lesson_id, imageULR, desc):
	o = Offer()
	o.course_id = course_id
	o.creater = creater
	o.language = language
	o.lesson_id = lesson_id
	o.imageULR = imageULR
	o.desc = desc
	o.put()
'''
class Lesson(db.Model):
	lesson_id = db.IntegerProperty(required = True)
	lesson_title = db.StringProperty(required = True)
	author = db.StringProperty(required = True)
	vocabulary = ObjectProperty()
	imgURLs = ObjectProperty()
	source_language = db.StringProperty(required = True)
	destination_language = db.StringProperty(required = True)
	questions = ObjectProperty()
	answers = ObjectProperty()
	notes = db.StringProperty()
'''
class ChineseLesson01(c_id, english, chinese, imageULR, notes, question_answer):
	l = Lesson()
	l.lesson_id = c_id
	l.english = english
	l.translation = chinese
	l.imageULR = imageULR
	l.notes = notes
	l.question_answer = question_answer
	l.put()
'''