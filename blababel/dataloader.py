from google.appengine.ext import db
from schema import *


# the following code is loading build-in Course data
desc = '''&nbsp&nbsp&nbsp Official language of the People's Republic of China, 
Taiwan, and Singapore.About one-fifth of the world's population, 
or over one billion people, speaks some form of Chinese as their first language.
'''

course = Course(course_id=1, 
				course_title='Chinese', 
				author='admin', 
				source_language='Chinese', 
				destination_language='English',
				imgURL='/img/course/chinese.jpg', 
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

'''
lesson = Lesson(course_id=%d,
				lesson_id=%d,
				lesson_title=%s, 
				author=%s,
				difficulty='beginner',
				source_language='img/lesson/cn%d',
				destination_language=%s,
				entries=entry_lists,
				questions=['','',''],
				answers=['','',''],
				notes=%s)
lesson.put()
'''

'''
entry = Entry(entry_id = %d,
			lesson_id = %d,
			imgURLs = 'img/lesson/cn%d',
			word = %s,
			mean = %s,
			source_language = %s,
			destination_language = %s,
			notes = %s)
entry.put()
'''

entry = Entry(entry_id = i,
			lesson_id = l_id,
			imgURLs = img[i],
			word = voca[i],
			mean = means[i],
			source_language = src,
			destination_language = dest,
			notes = note)
entry.put()