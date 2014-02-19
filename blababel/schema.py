from classes.ObjectProperty import ObjectProperty
from google.appengine.ext import db


###########################################
#
# Seperated from handler.py 
#
###########################################
class User(db.Model):
	firstname = db.StringProperty(required = True)
	lastname = db.StringProperty(required = True)
	email = db.StringProperty(required = True)
	username = db.StringProperty(required = True)
	password = db.StringProperty(required = True)

class UserProfile(db.Model):
	uid = db. IntegerProperty(required=True)
	username = db.StringProperty(required = True) 
	courses = ObjectProperty()
	scores = ObjectProperty()

class Course(db.Model):
	course_id = db.IntegerProperty(required = True)
	course_title = db.StringProperty(required = True)
	author = db.StringProperty(required = True)
	source_language = db.StringProperty(required = True)
	destination_language = db.StringProperty(required = True)
	imgURL = db.StringProperty(required = True)
	course_description = db.StringProperty()
	lessons = ObjectProperty()

class Lesson(db.Model):
	course_id = db.IntegerProperty(required = True)
	lesson_id = db.IntegerProperty(required = True)
	lesson_title = db.StringProperty(required = True)
	author = db.StringProperty(required = True)
	difficulty = db.StringProperty(required = True)
	source_language = db.StringProperty(required = True)
	destination_language = db.StringProperty(required = True)
	entries = ObjectProperty()
	questions = ObjectProperty()
	answers = ObjectProperty()
	notes = db.StringProperty()

class Entry(db.Model):
	entry_id = db.IntegerProperty(required = True)
	lesson_id = db.IntegerProperty(required = True)
	imgURLs = ObjectProperty()
	word = db.StringProperty(required=True)
	mean = db.StringProperty(required=True)
	source_language = db.StringProperty(required = True)
	destination_language = db.StringProperty(required = True)
	notes = db.StringProperty()