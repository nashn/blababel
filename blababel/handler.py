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
		courses = db.GqlQuery("SELECT * FROM Course").fetch(10)
		tvalues = {'authors': authors,
		'courses': courses
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
		
		course = Course(course_id=c_id, course_title=c_title, 
			author=author, imgURL=c_img, course_description=desc, 
			source_language=src, destination_language=dest)
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
		
		lesson = Lesson(course_id=c_id, lesson_id=l_id, lesson_title=l_title, 
			difficulty=difficulty, author=author, vocabulary=vocabulary, 
			imgURLs=images, questions=q, answers=a, notes=notes, 
			source_language=src, destination_language=dest)
		lesson.put()

		l = db.GqlQuery("SELECT * FROM Lesson WHERE lesson_id=%d" % l_id).get()
		s = "Success! Here is the entry:\n"
		s += "%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s" % (l.course_id,
			l.lesson_id, l.lesson_title, l.difficulty, l.author, 
			l.vocabulary, l.imgURLs, l.questions, l.answers,
			l.notes, l.source_language, l.destination_language)
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

class Course(db.Model):
	course_id = db.IntegerProperty(required = True)
	course_title = db.StringProperty(required = True)
	author = db.StringProperty(required = True)
	source_language = db.StringProperty(required = True)
	destination_language = db.StringProperty(required = True)
	imgURL = db.StringProperty(required = True)
	course_description = db.StringProperty()

class Lesson(db.Model):
	course_id = db.IntegerProperty(required = True)
	lesson_id = db.IntegerProperty(required = True)
	lesson_title = db.StringProperty(required = True)
	author = db.StringProperty(required = True)
	difficulty = db.StringProperty(required = True)
	vocabulary = ObjectProperty()
	imgURLs = ObjectProperty()
	source_language = db.StringProperty(required = True)
	destination_language = db.StringProperty(required = True)
	questions = ObjectProperty()
	answers = ObjectProperty()
	notes = db.StringProperty()