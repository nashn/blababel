from google.appengine.ext import db
from schema import *


def load():
	# the following code is loading build-in Course data
	desc = '''&nbsp&nbsp&nbsp Official language of the People's Republic of China, Taiwan, and Singapore.About one-fifth of the world's population, or over one billion people, speaks some form of Chinese as their first language.'''

	course = Course(course_id=1, 
					course_title='Chinese', 
					author='admin', 
					source_language='Chinese', 
					destination_language='English',
					imgURL='\"/img/course/chinese.jpg\"', 
					course_description=desc, 
					lessons=[1,2,3])
	course.put()

	course = Course(course_id=2, 
					course_title='Korean', 
					author='admin', 
					source_language='Korean', 
					destination_language='English',
					imgURL='/img/course/chinese.jpg', 
					course_description=desc, 
					lessons=[1,2,3])
	course.put()

	course = Course(course_id=1, 
					course_title='Japanese', 
					author='admin', 
					source_language='Japanese', 
					destination_language='English',
					imgURL='/img/course/chinese.jpg', 
					course_description=desc, 
					lessons=[1,2,3])
	course.put()


	#########################################################################
	#########################################################################
	#########################################################################

	# the following is loading build-in Lesson data


	lesson = Lesson(course_id=1,
			lesson_id=1,
			lesson_title='lesson-1', 
			author='admin',
			difficulty='beginner',
			source_language='Chinese',
			destination_language='English',
			entries=[1,2,3,4,5,6,7,8],
			questions=['','',''],
			answers=['','',''],
			notes='This is only for testing the data function.')

	lesson.put()

	entry = Entry(entry_id = 1,
			lesson_id = 1,
			imgURLs = 'img/lesson/cn1',
			word = 'man',
			mean = 'nanren',
			source_language = 'Chinese',
			destination_language = 'English',
			notes = 'This is only for testing the data function.')

	entry.put()

	entry = Entry(entry_id = 2,
			lesson_id = 1,
			imgURLs = 'img/lesson/cn2',
			word = 'girl',
			mean = 'nvhai',
			source_language = 'Chinese',
			destination_language = 'English',
			notes = 'This is only for testing the data function.')

	entry.put()

	entry = Entry(entry_id = 3,
			lesson_id = 1,
			imgURLs = 'img/lesson/cn3',
			word = 'woman',
			mean = 'nvren',
			source_language = 'Chinese',
			destination_language = 'English',
			notes = 'This is only for testing the data function.')

	entry.put()

	entry = Entry(entry_id = 4,
			lesson_id = 1,
			imgURLs = 'img/lesson/cn4',
			word = 'apple',
			mean = 'pinguo',
			source_language = 'Chinese',
			destination_language = 'English',
			notes = 'This is only for testing the data function.')

	entry.put()

	entry = Entry(entry_id = 5,
			lesson_id = 1,
			imgURLs = 'img/lesson/cn5',
			word = 'banana',
			mean = 'xiangjiao',
			source_language = 'Chinese',
			destination_language = 'English',
			notes = 'This is only for testing the data function.')

	entry.put()

	entry = Entry(entry_id = 6,
			lesson_id = 1,
			imgURLs = 'img/lesson/cn6',
			word = 'pear',
			mean = 'pingguodiannao',
			source_language = 'Chinese',
			destination_language = 'English',
			notes = 'This is only for testing the data function.')

	entry.put()

	entry = Entry(entry_id = 7,
			lesson_id = 1,
			imgURLs = 'img/lesson/cn7',
			word = 'mac',
			mean = 'linuxxitong',
			source_language = 'Chinese',
			destination_language = 'English',
			notes = 'This is only for testing the data function.')

	entry.put()

	entry = Entry(entry_id = 8,
			lesson_id = 1,
			imgURLs = 'img/lesson/cn8',
			word = 'ubuntu',
			mean = 'laji',
			source_language = 'Chinese',
			destination_language = 'English',
			notes = 'This is only for testing the data function.')

	entry.put()

	lesson = Lesson(course_id=1,
			lesson_id=2,
			lesson_title='lesson-2', 
			author='admin',
			difficulty='beginner',
			source_language='Chinese',
			destination_language='English',
			entries=[1,2,3,4,5,6,7,8],
			questions=['','',''],
			answers=['','',''],
			notes='This is only for testing the data function.')

	lesson.put()

	entry = Entry(entry_id = 1,
			lesson_id = 2,
			imgURLs = 'img/lesson/cn1',
			word = 'man',
			mean = 'nanren',
			source_language = 'Chinese',
			destination_language = 'English',
			notes = 'This is only for testing the data function.')

	entry.put()

	entry = Entry(entry_id = 2,
			lesson_id = 2,
			imgURLs = 'img/lesson/cn2',
			word = 'girl',
			mean = 'nvhai',
			source_language = 'Chinese',
			destination_language = 'English',
			notes = 'This is only for testing the data function.')

	entry.put()

	entry = Entry(entry_id = 3,
			lesson_id = 2,
			imgURLs = 'img/lesson/cn3',
			word = 'woman',
			mean = 'nvren',
			source_language = 'Chinese',
			destination_language = 'English',
			notes = 'This is only for testing the data function.')

	entry.put()

	entry = Entry(entry_id = 4,
			lesson_id = 2,
			imgURLs = 'img/lesson/cn4',
			word = 'apple',
			mean = 'pinguo',
			source_language = 'Chinese',
			destination_language = 'English',
			notes = 'This is only for testing the data function.')

	entry.put()

	entry = Entry(entry_id = 5,
			lesson_id = 2,
			imgURLs = 'img/lesson/cn5',
			word = 'banana',
			mean = 'xiangjiao',
			source_language = 'Chinese',
			destination_language = 'English',
			notes = 'This is only for testing the data function.')

	entry.put()

	entry = Entry(entry_id = 6,
			lesson_id = 2,
			imgURLs = 'img/lesson/cn6',
			word = 'pear',
			mean = 'pingguodiannao',
			source_language = 'Chinese',
			destination_language = 'English',
			notes = 'This is only for testing the data function.')

	entry.put()

	entry = Entry(entry_id = 7,
			lesson_id = 2,
			imgURLs = 'img/lesson/cn7',
			word = 'mac',
			mean = 'linuxxitong',
			source_language = 'Chinese',
			destination_language = 'English',
			notes = 'This is only for testing the data function.')

	entry.put()

	entry = Entry(entry_id = 8,
			lesson_id = 2,
			imgURLs = 'img/lesson/cn8',
			word = 'ubuntu',
			mean = 'laji',
			source_language = 'Chinese',
			destination_language = 'English',
			notes = 'This is only for testing the data function.')

	entry.put()

	lesson = Lesson(course_id=1,
			lesson_id=3,
			lesson_title='lesson-3', 
			author='admin',
			difficulty='beginner',
			source_language='Chinese',
			destination_language='English',
			entries=[1,2,3,4,5,6,7,8],
			questions=['','',''],
			answers=['','',''],
			notes='This is only for testing the data function.')

	lesson.put()

	entry = Entry(entry_id = 1,
			lesson_id = 3,
			imgURLs = 'img/lesson/cn1',
			word = 'man',
			mean = 'nanren',
			source_language = 'Chinese',
			destination_language = 'English',
			notes = 'This is only for testing the data function.')

	entry.put()

	entry = Entry(entry_id = 2,
			lesson_id = 3,
			imgURLs = 'img/lesson/cn2',
			word = 'girl',
			mean = 'nvhai',
			source_language = 'Chinese',
			destination_language = 'English',
			notes = 'This is only for testing the data function.')

	entry.put()

	entry = Entry(entry_id = 3,
			lesson_id = 3,
			imgURLs = 'img/lesson/cn3',
			word = 'woman',
			mean = 'nvren',
			source_language = 'Chinese',
			destination_language = 'English',
			notes = 'This is only for testing the data function.')

	entry.put()

	entry = Entry(entry_id = 4,
			lesson_id = 3,
			imgURLs = 'img/lesson/cn4',
			word = 'apple',
			mean = 'pinguo',
			source_language = 'Chinese',
			destination_language = 'English',
			notes = 'This is only for testing the data function.')

	entry.put()

	entry = Entry(entry_id = 5,
			lesson_id = 3,
			imgURLs = 'img/lesson/cn5',
			word = 'banana',
			mean = 'xiangjiao',
			source_language = 'Chinese',
			destination_language = 'English',
			notes = 'This is only for testing the data function.')

	entry.put()

	entry = Entry(entry_id = 6,
			lesson_id = 3,
			imgURLs = 'img/lesson/cn6',
			word = 'pear',
			mean = 'pingguodiannao',
			source_language = 'Chinese',
			destination_language = 'English',
			notes = 'This is only for testing the data function.')

	entry.put()

	entry = Entry(entry_id = 7,
			lesson_id = 3,
			imgURLs = 'img/lesson/cn7',
			word = 'mac',
			mean = 'linuxxitong',
			source_language = 'Chinese',
			destination_language = 'English',
			notes = 'This is only for testing the data function.')

	entry.put()

	entry = Entry(entry_id = 8,
			lesson_id = 3,
			imgURLs = 'img/lesson/cn8',
			word = 'ubuntu',
			mean = 'laji',
			source_language = 'Chinese',
			destination_language = 'English',
			notes = 'This is only for testing the data function.')

	entry.put()

	lesson = Lesson(course_id=1,
			lesson_id=4,
			lesson_title='lesson-4', 
			author='admin',
			difficulty='beginner',
			source_language='Chinese',
			destination_language='English',
			entries=[1,2,3,4,5,6,7,8],
			questions=['','',''],
			answers=['','',''],
			notes='This is only for testing the data function.')

	lesson.put()

	entry = Entry(entry_id = 1,
			lesson_id = 4,
			imgURLs = 'img/lesson/cn1',
			word = 'man',
			mean = 'nanren',
			source_language = 'Chinese',
			destination_language = 'English',
			notes = 'This is only for testing the data function.')

	entry.put()

	entry = Entry(entry_id = 2,
			lesson_id = 4,
			imgURLs = 'img/lesson/cn2',
			word = 'girl',
			mean = 'nvhai',
			source_language = 'Chinese',
			destination_language = 'English',
			notes = 'This is only for testing the data function.')

	entry.put()

	entry = Entry(entry_id = 3,
			lesson_id = 4,
			imgURLs = 'img/lesson/cn3',
			word = 'woman',
			mean = 'nvren',
			source_language = 'Chinese',
			destination_language = 'English',
			notes = 'This is only for testing the data function.')

	entry.put()

	entry = Entry(entry_id = 4,
			lesson_id = 4,
			imgURLs = 'img/lesson/cn4',
			word = 'apple',
			mean = 'pinguo',
			source_language = 'Chinese',
			destination_language = 'English',
			notes = 'This is only for testing the data function.')

	entry.put()

	entry = Entry(entry_id = 5,
			lesson_id = 4,
			imgURLs = 'img/lesson/cn5',
			word = 'banana',
			mean = 'xiangjiao',
			source_language = 'Chinese',
			destination_language = 'English',
			notes = 'This is only for testing the data function.')

	entry.put()

	entry = Entry(entry_id = 6,
			lesson_id = 4,
			imgURLs = 'img/lesson/cn6',
			word = 'pear',
			mean = 'pingguodiannao',
			source_language = 'Chinese',
			destination_language = 'English',
			notes = 'This is only for testing the data function.')

	entry.put()

	entry = Entry(entry_id = 7,
			lesson_id = 4,
			imgURLs = 'img/lesson/cn7',
			word = 'mac',
			mean = 'linuxxitong',
			source_language = 'Chinese',
			destination_language = 'English',
			notes = 'This is only for testing the data function.')

	entry.put()

	entry = Entry(entry_id = 8,
			lesson_id = 4,
			imgURLs = 'img/lesson/cn8',
			word = 'ubuntu',
			mean = 'laji',
			source_language = 'Chinese',
			destination_language = 'English',
			notes = 'This is only for testing the data function.')

	entry.put()

	lesson = Lesson(course_id=2,
			lesson_id=1,
			lesson_title='lesson-1', 
			author='admin',
			difficulty='beginner',
			source_language='Korean',
			destination_language='English',
			entries=[1,2,3,4,5,6,7,8],
			questions=['','',''],
			answers=['','',''],
			notes='This is only for testing the data function.')

	lesson.put()

	entry = Entry(entry_id = 1,
			lesson_id = 1,
			imgURLs = 'img/lesson/cn1',
			word = 'man',
			mean = 'nanren',
			source_language = 'Korean',
			destination_language = 'English',
			notes = 'This is only for testing the data function.')

	entry.put()

	entry = Entry(entry_id = 2,
			lesson_id = 1,
			imgURLs = 'img/lesson/cn2',
			word = 'girl',
			mean = 'nvhai',
			source_language = 'Korean',
			destination_language = 'English',
			notes = 'This is only for testing the data function.')

	entry.put()

	entry = Entry(entry_id = 3,
			lesson_id = 1,
			imgURLs = 'img/lesson/cn3',
			word = 'woman',
			mean = 'nvren',
			source_language = 'Korean',
			destination_language = 'English',
			notes = 'This is only for testing the data function.')

	entry.put()

	entry = Entry(entry_id = 4,
			lesson_id = 1,
			imgURLs = 'img/lesson/cn4',
			word = 'apple',
			mean = 'pinguo',
			source_language = 'Korean',
			destination_language = 'English',
			notes = 'This is only for testing the data function.')

	entry.put()

	entry = Entry(entry_id = 5,
			lesson_id = 1,
			imgURLs = 'img/lesson/cn5',
			word = 'banana',
			mean = 'xiangjiao',
			source_language = 'Korean',
			destination_language = 'English',
			notes = 'This is only for testing the data function.')

	entry.put()

	entry = Entry(entry_id = 6,
			lesson_id = 1,
			imgURLs = 'img/lesson/cn6',
			word = 'pear',
			mean = 'pingguodiannao',
			source_language = 'Korean',
			destination_language = 'English',
			notes = 'This is only for testing the data function.')

	entry.put()

	entry = Entry(entry_id = 7,
			lesson_id = 1,
			imgURLs = 'img/lesson/cn7',
			word = 'mac',
			mean = 'linuxxitong',
			source_language = 'Korean',
			destination_language = 'English',
			notes = 'This is only for testing the data function.')

	entry.put()

	entry = Entry(entry_id = 8,
			lesson_id = 1,
			imgURLs = 'img/lesson/cn8',
			word = 'ubuntu',
			mean = 'laji',
			source_language = 'Korean',
			destination_language = 'English',
			notes = 'This is only for testing the data function.')

	entry.put()

	lesson = Lesson(course_id=2,
			lesson_id=2,
			lesson_title='lesson-2', 
			author='admin',
			difficulty='beginner',
			source_language='Korean',
			destination_language='English',
			entries=[1,2,3,4,5,6,7,8],
			questions=['','',''],
			answers=['','',''],
			notes='This is only for testing the data function.')

	lesson.put()

	entry = Entry(entry_id = 1,
			lesson_id = 2,
			imgURLs = 'img/lesson/cn1',
			word = 'man',
			mean = 'nanren',
			source_language = 'Korean',
			destination_language = 'English',
			notes = 'This is only for testing the data function.')

	entry.put()

	entry = Entry(entry_id = 2,
			lesson_id = 2,
			imgURLs = 'img/lesson/cn2',
			word = 'girl',
			mean = 'nvhai',
			source_language = 'Korean',
			destination_language = 'English',
			notes = 'This is only for testing the data function.')

	entry.put()

	entry = Entry(entry_id = 3,
			lesson_id = 2,
			imgURLs = 'img/lesson/cn3',
			word = 'woman',
			mean = 'nvren',
			source_language = 'Korean',
			destination_language = 'English',
			notes = 'This is only for testing the data function.')

	entry.put()

	entry = Entry(entry_id = 4,
			lesson_id = 2,
			imgURLs = 'img/lesson/cn4',
			word = 'apple',
			mean = 'pinguo',
			source_language = 'Korean',
			destination_language = 'English',
			notes = 'This is only for testing the data function.')

	entry.put()

	entry = Entry(entry_id = 5,
			lesson_id = 2,
			imgURLs = 'img/lesson/cn5',
			word = 'banana',
			mean = 'xiangjiao',
			source_language = 'Korean',
			destination_language = 'English',
			notes = 'This is only for testing the data function.')

	entry.put()

	entry = Entry(entry_id = 6,
			lesson_id = 2,
			imgURLs = 'img/lesson/cn6',
			word = 'pear',
			mean = 'pingguodiannao',
			source_language = 'Korean',
			destination_language = 'English',
			notes = 'This is only for testing the data function.')

	entry.put()

	entry = Entry(entry_id = 7,
			lesson_id = 2,
			imgURLs = 'img/lesson/cn7',
			word = 'mac',
			mean = 'linuxxitong',
			source_language = 'Korean',
			destination_language = 'English',
			notes = 'This is only for testing the data function.')

	entry.put()

	entry = Entry(entry_id = 8,
			lesson_id = 2,
			imgURLs = 'img/lesson/cn8',
			word = 'ubuntu',
			mean = 'laji',
			source_language = 'Korean',
			destination_language = 'English',
			notes = 'This is only for testing the data function.')

	entry.put()

	lesson = Lesson(course_id=2,
			lesson_id=3,
			lesson_title='lesson-3', 
			author='admin',
			difficulty='beginner',
			source_language='Korean',
			destination_language='English',
			entries=[1,2,3,4,5,6,7,8],
			questions=['','',''],
			answers=['','',''],
			notes='This is only for testing the data function.')

	lesson.put()

	entry = Entry(entry_id = 1,
			lesson_id = 3,
			imgURLs = 'img/lesson/cn1',
			word = 'man',
			mean = 'nanren',
			source_language = 'Korean',
			destination_language = 'English',
			notes = 'This is only for testing the data function.')

	entry.put()

	entry = Entry(entry_id = 2,
			lesson_id = 3,
			imgURLs = 'img/lesson/cn2',
			word = 'girl',
			mean = 'nvhai',
			source_language = 'Korean',
			destination_language = 'English',
			notes = 'This is only for testing the data function.')

	entry.put()

	entry = Entry(entry_id = 3,
			lesson_id = 3,
			imgURLs = 'img/lesson/cn3',
			word = 'woman',
			mean = 'nvren',
			source_language = 'Korean',
			destination_language = 'English',
			notes = 'This is only for testing the data function.')

	entry.put()

	entry = Entry(entry_id = 4,
			lesson_id = 3,
			imgURLs = 'img/lesson/cn4',
			word = 'apple',
			mean = 'pinguo',
			source_language = 'Korean',
			destination_language = 'English',
			notes = 'This is only for testing the data function.')

	entry.put()

	entry = Entry(entry_id = 5,
			lesson_id = 3,
			imgURLs = 'img/lesson/cn5',
			word = 'banana',
			mean = 'xiangjiao',
			source_language = 'Korean',
			destination_language = 'English',
			notes = 'This is only for testing the data function.')

	entry.put()

	entry = Entry(entry_id = 6,
			lesson_id = 3,
			imgURLs = 'img/lesson/cn6',
			word = 'pear',
			mean = 'pingguodiannao',
			source_language = 'Korean',
			destination_language = 'English',
			notes = 'This is only for testing the data function.')

	entry.put()

	entry = Entry(entry_id = 7,
			lesson_id = 3,
			imgURLs = 'img/lesson/cn7',
			word = 'mac',
			mean = 'linuxxitong',
			source_language = 'Korean',
			destination_language = 'English',
			notes = 'This is only for testing the data function.')

	entry.put()

	entry = Entry(entry_id = 8,
			lesson_id = 3,
			imgURLs = 'img/lesson/cn8',
			word = 'ubuntu',
			mean = 'laji',
			source_language = 'Korean',
			destination_language = 'English',
			notes = 'This is only for testing the data function.')

	entry.put()

	lesson = Lesson(course_id=2,
			lesson_id=4,
			lesson_title='lesson-4', 
			author='admin',
			difficulty='beginner',
			source_language='Korean',
			destination_language='English',
			entries=[1,2,3,4,5,6,7,8],
			questions=['','',''],
			answers=['','',''],
			notes='This is only for testing the data function.')

	lesson.put()

	entry = Entry(entry_id = 1,
			lesson_id = 4,
			imgURLs = 'img/lesson/cn1',
			word = 'man',
			mean = 'nanren',
			source_language = 'Korean',
			destination_language = 'English',
			notes = 'This is only for testing the data function.')

	entry.put()

	entry = Entry(entry_id = 2,
			lesson_id = 4,
			imgURLs = 'img/lesson/cn2',
			word = 'girl',
			mean = 'nvhai',
			source_language = 'Korean',
			destination_language = 'English',
			notes = 'This is only for testing the data function.')

	entry.put()

	entry = Entry(entry_id = 3,
			lesson_id = 4,
			imgURLs = 'img/lesson/cn3',
			word = 'woman',
			mean = 'nvren',
			source_language = 'Korean',
			destination_language = 'English',
			notes = 'This is only for testing the data function.')

	entry.put()

	entry = Entry(entry_id = 4,
			lesson_id = 4,
			imgURLs = 'img/lesson/cn4',
			word = 'apple',
			mean = 'pinguo',
			source_language = 'Korean',
			destination_language = 'English',
			notes = 'This is only for testing the data function.')

	entry.put()

	entry = Entry(entry_id = 5,
			lesson_id = 4,
			imgURLs = 'img/lesson/cn5',
			word = 'banana',
			mean = 'xiangjiao',
			source_language = 'Korean',
			destination_language = 'English',
			notes = 'This is only for testing the data function.')

	entry.put()

	entry = Entry(entry_id = 6,
			lesson_id = 4,
			imgURLs = 'img/lesson/cn6',
			word = 'pear',
			mean = 'pingguodiannao',
			source_language = 'Korean',
			destination_language = 'English',
			notes = 'This is only for testing the data function.')

	entry.put()

	entry = Entry(entry_id = 7,
			lesson_id = 4,
			imgURLs = 'img/lesson/cn7',
			word = 'mac',
			mean = 'linuxxitong',
			source_language = 'Korean',
			destination_language = 'English',
			notes = 'This is only for testing the data function.')

	entry.put()

	entry = Entry(entry_id = 8,
			lesson_id = 4,
			imgURLs = 'img/lesson/cn8',
			word = 'ubuntu',
			mean = 'laji',
			source_language = 'Korean',
			destination_language = 'English',
			notes = 'This is only for testing the data function.')

	entry.put()

	lesson = Lesson(course_id=3,
			lesson_id=1,
			lesson_title='lesson-1', 
			author='admin',
			difficulty='beginner',
			source_language='Japanese',
			destination_language='English',
			entries=[1,2,3,4,5,6,7,8],
			questions=['','',''],
			answers=['','',''],
			notes='This is only for testing the data function.')

	lesson.put()

	entry = Entry(entry_id = 1,
			lesson_id = 1,
			imgURLs = 'img/lesson/cn1',
			word = 'man',
			mean = 'nanren',
			source_language = 'Japanese',
			destination_language = 'English',
			notes = 'This is only for testing the data function.')

	entry.put()

	entry = Entry(entry_id = 2,
			lesson_id = 1,
			imgURLs = 'img/lesson/cn2',
			word = 'girl',
			mean = 'nvhai',
			source_language = 'Japanese',
			destination_language = 'English',
			notes = 'This is only for testing the data function.')

	entry.put()

	entry = Entry(entry_id = 3,
			lesson_id = 1,
			imgURLs = 'img/lesson/cn3',
			word = 'woman',
			mean = 'nvren',
			source_language = 'Japanese',
			destination_language = 'English',
			notes = 'This is only for testing the data function.')

	entry.put()

	entry = Entry(entry_id = 4,
			lesson_id = 1,
			imgURLs = 'img/lesson/cn4',
			word = 'apple',
			mean = 'pinguo',
			source_language = 'Japanese',
			destination_language = 'English',
			notes = 'This is only for testing the data function.')

	entry.put()

	entry = Entry(entry_id = 5,
			lesson_id = 1,
			imgURLs = 'img/lesson/cn5',
			word = 'banana',
			mean = 'xiangjiao',
			source_language = 'Japanese',
			destination_language = 'English',
			notes = 'This is only for testing the data function.')

	entry.put()

	entry = Entry(entry_id = 6,
			lesson_id = 1,
			imgURLs = 'img/lesson/cn6',
			word = 'pear',
			mean = 'pingguodiannao',
			source_language = 'Japanese',
			destination_language = 'English',
			notes = 'This is only for testing the data function.')

	entry.put()

	entry = Entry(entry_id = 7,
			lesson_id = 1,
			imgURLs = 'img/lesson/cn7',
			word = 'mac',
			mean = 'linuxxitong',
			source_language = 'Japanese',
			destination_language = 'English',
			notes = 'This is only for testing the data function.')

	entry.put()

	entry = Entry(entry_id = 8,
			lesson_id = 1,
			imgURLs = 'img/lesson/cn8',
			word = 'ubuntu',
			mean = 'laji',
			source_language = 'Japanese',
			destination_language = 'English',
			notes = 'This is only for testing the data function.')

	entry.put()

	lesson = Lesson(course_id=3,
			lesson_id=2,
			lesson_title='lesson-2', 
			author='admin',
			difficulty='beginner',
			source_language='Japanese',
			destination_language='English',
			entries=[1,2,3,4,5,6,7,8],
			questions=['','',''],
			answers=['','',''],
			notes='This is only for testing the data function.')

	lesson.put()

	entry = Entry(entry_id = 1,
			lesson_id = 2,
			imgURLs = 'img/lesson/cn1',
			word = 'man',
			mean = 'nanren',
			source_language = 'Japanese',
			destination_language = 'English',
			notes = 'This is only for testing the data function.')

	entry.put()

	entry = Entry(entry_id = 2,
			lesson_id = 2,
			imgURLs = 'img/lesson/cn2',
			word = 'girl',
			mean = 'nvhai',
			source_language = 'Japanese',
			destination_language = 'English',
			notes = 'This is only for testing the data function.')

	entry.put()

	entry = Entry(entry_id = 3,
			lesson_id = 2,
			imgURLs = 'img/lesson/cn3',
			word = 'woman',
			mean = 'nvren',
			source_language = 'Japanese',
			destination_language = 'English',
			notes = 'This is only for testing the data function.')

	entry.put()

	entry = Entry(entry_id = 4,
			lesson_id = 2,
			imgURLs = 'img/lesson/cn4',
			word = 'apple',
			mean = 'pinguo',
			source_language = 'Japanese',
			destination_language = 'English',
			notes = 'This is only for testing the data function.')

	entry.put()

	entry = Entry(entry_id = 5,
			lesson_id = 2,
			imgURLs = 'img/lesson/cn5',
			word = 'banana',
			mean = 'xiangjiao',
			source_language = 'Japanese',
			destination_language = 'English',
			notes = 'This is only for testing the data function.')

	entry.put()

	entry = Entry(entry_id = 6,
			lesson_id = 2,
			imgURLs = 'img/lesson/cn6',
			word = 'pear',
			mean = 'pingguodiannao',
			source_language = 'Japanese',
			destination_language = 'English',
			notes = 'This is only for testing the data function.')

	entry.put()

	entry = Entry(entry_id = 7,
			lesson_id = 2,
			imgURLs = 'img/lesson/cn7',
			word = 'mac',
			mean = 'linuxxitong',
			source_language = 'Japanese',
			destination_language = 'English',
			notes = 'This is only for testing the data function.')

	entry.put()

	entry = Entry(entry_id = 8,
			lesson_id = 2,
			imgURLs = 'img/lesson/cn8',
			word = 'ubuntu',
			mean = 'laji',
			source_language = 'Japanese',
			destination_language = 'English',
			notes = 'This is only for testing the data function.')

	entry.put()

	lesson = Lesson(course_id=3,
			lesson_id=3,
			lesson_title='lesson-3', 
			author='admin',
			difficulty='beginner',
			source_language='Japanese',
			destination_language='English',
			entries=[1,2,3,4,5,6,7,8],
			questions=['','',''],
			answers=['','',''],
			notes='This is only for testing the data function.')

	lesson.put()

	entry = Entry(entry_id = 1,
			lesson_id = 3,
			imgURLs = 'img/lesson/cn1',
			word = 'man',
			mean = 'nanren',
			source_language = 'Japanese',
			destination_language = 'English',
			notes = 'This is only for testing the data function.')

	entry.put()

	entry = Entry(entry_id = 2,
			lesson_id = 3,
			imgURLs = 'img/lesson/cn2',
			word = 'girl',
			mean = 'nvhai',
			source_language = 'Japanese',
			destination_language = 'English',
			notes = 'This is only for testing the data function.')

	entry.put()

	entry = Entry(entry_id = 3,
			lesson_id = 3,
			imgURLs = 'img/lesson/cn3',
			word = 'woman',
			mean = 'nvren',
			source_language = 'Japanese',
			destination_language = 'English',
			notes = 'This is only for testing the data function.')

	entry.put()

	entry = Entry(entry_id = 4,
			lesson_id = 3,
			imgURLs = 'img/lesson/cn4',
			word = 'apple',
			mean = 'pinguo',
			source_language = 'Japanese',
			destination_language = 'English',
			notes = 'This is only for testing the data function.')

	entry.put()

	entry = Entry(entry_id = 5,
			lesson_id = 3,
			imgURLs = 'img/lesson/cn5',
			word = 'banana',
			mean = 'xiangjiao',
			source_language = 'Japanese',
			destination_language = 'English',
			notes = 'This is only for testing the data function.')

	entry.put()

	entry = Entry(entry_id = 6,
			lesson_id = 3,
			imgURLs = 'img/lesson/cn6',
			word = 'pear',
			mean = 'pingguodiannao',
			source_language = 'Japanese',
			destination_language = 'English',
			notes = 'This is only for testing the data function.')

	entry.put()

	entry = Entry(entry_id = 7,
			lesson_id = 3,
			imgURLs = 'img/lesson/cn7',
			word = 'mac',
			mean = 'linuxxitong',
			source_language = 'Japanese',
			destination_language = 'English',
			notes = 'This is only for testing the data function.')

	entry.put()

	entry = Entry(entry_id = 8,
			lesson_id = 3,
			imgURLs = 'img/lesson/cn8',
			word = 'ubuntu',
			mean = 'laji',
			source_language = 'Japanese',
			destination_language = 'English',
			notes = 'This is only for testing the data function.')

	entry.put()

	lesson = Lesson(course_id=3,
			lesson_id=4,
			lesson_title='lesson-4', 
			author='admin',
			difficulty='beginner',
			source_language='Japanese',
			destination_language='English',
			entries=[1,2,3,4,5,6,7,8],
			questions=['','',''],
			answers=['','',''],
			notes='This is only for testing the data function.')

	lesson.put()

	entry = Entry(entry_id = 1,
			lesson_id = 4,
			imgURLs = 'img/lesson/cn1',
			word = 'man',
			mean = 'nanren',
			source_language = 'Japanese',
			destination_language = 'English',
			notes = 'This is only for testing the data function.')

	entry.put()

	entry = Entry(entry_id = 2,
			lesson_id = 4,
			imgURLs = 'img/lesson/cn2',
			word = 'girl',
			mean = 'nvhai',
			source_language = 'Japanese',
			destination_language = 'English',
			notes = 'This is only for testing the data function.')

	entry.put()

	entry = Entry(entry_id = 3,
			lesson_id = 4,
			imgURLs = 'img/lesson/cn3',
			word = 'woman',
			mean = 'nvren',
			source_language = 'Japanese',
			destination_language = 'English',
			notes = 'This is only for testing the data function.')

	entry.put()

	entry = Entry(entry_id = 4,
			lesson_id = 4,
			imgURLs = 'img/lesson/cn4',
			word = 'apple',
			mean = 'pinguo',
			source_language = 'Japanese',
			destination_language = 'English',
			notes = 'This is only for testing the data function.')

	entry.put()

	entry = Entry(entry_id = 5,
			lesson_id = 4,
			imgURLs = 'img/lesson/cn5',
			word = 'banana',
			mean = 'xiangjiao',
			source_language = 'Japanese',
			destination_language = 'English',
			notes = 'This is only for testing the data function.')

	entry.put()

	entry = Entry(entry_id = 6,
			lesson_id = 4,
			imgURLs = 'img/lesson/cn6',
			word = 'pear',
			mean = 'pingguodiannao',
			source_language = 'Japanese',
			destination_language = 'English',
			notes = 'This is only for testing the data function.')

	entry.put()

	entry = Entry(entry_id = 7,
			lesson_id = 4,
			imgURLs = 'img/lesson/cn7',
			word = 'mac',
			mean = 'linuxxitong',
			source_language = 'Japanese',
			destination_language = 'English',
			notes = 'This is only for testing the data function.')

	entry.put()

	entry = Entry(entry_id = 8,
			lesson_id = 4,
			imgURLs = 'img/lesson/cn8',
			word = 'ubuntu',
			mean = 'laji',
			source_language = 'Japanese',
			destination_language = 'English',
			notes = 'This is only for testing the data function.')

	entry.put()
