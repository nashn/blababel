# !/usr/python2.7
# handler.py

'''
Adding a new page with a new handlers
Maybe change to generic handler class later
'''
import os
import webapp2
import jinja2
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

# this may be used to handle error situation later
class ErrorPage(Handler):
	def get(self):
		tvalues = {'authors': authors,
					'teststring' : 'Hello World'
					}
		self.render('404.html', template_values=tvalues)
####################################

class LessonPage(Handler):
	def get(self):
		# entry = get from database

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
		entry01 = ChineseLesson01(english='Boy', chinese='男孩', imageULR='boy.png', notes=[])
		entry02 = ChineseLesson01(english='Girl', chinese='女孩', imageULR='girl.png', notes=[])
		entry03 = ChineseLesson01(english='Apple', chinese='苹果', imageULR='apple.png', notes=[])
		entry04 = ChineseLesson01(english='Woman', chinese='女人', imageULR='woman.png', notes=[])
		entry01.put()
		entry02.put()
		entry03.put()
		entry04.put()
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

class User(db.Model):
	firstname = db.StringProperty(required = True)
	lastname = db.StringProperty(required = True)
	email = db.StringProperty(required = True)
	password = db.StringProperty(required = True)

class ChineseLesson01(db.Model):
	english = db.StringProperty(required = True)
	chinese = db.StringProperty(required = True)
	imageULR = db.StringProperty(required = True)
	notes = db.StringProperty()
	
