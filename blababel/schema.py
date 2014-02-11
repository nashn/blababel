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