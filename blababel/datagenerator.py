# datagenerator.py
# created on 02/13/2014
# used for data generation
'''
lesson = lesson = Lesson(course_id=%d,
				lesson_id=%d,
				lesson_title=\'%s\', 
				author=\'%s\',
				difficulty='beginner',
				source_language=\'%s\',
				destination_language=\'%s\',
				entries=entry_lists,
				questions=['','',''],
				answers=['','',''],
				notes=\'%s\')
lesson.put()
'''
'''
entry = entry = Entry(entry_id = %d,
			lesson_id = %d,
			imgURLs = 'img/lesson/cn%d',
			word = \'%s\',
			mean = \'%s\',
			source_language = \'%s\',
			destination_language = \'%s\',
			notes = \'%s\')
entry.put()
'''

f = open('dataloader.txt', 'a')

course_info = [(1, 'Chinese', 'English'), 
				(2, 'Korean', 'English'), 
				(3, 'Japanese', 'English')]
note = 'This is only for testing the data function.'

# add new words here
word = ['boy', 'man', 'girl', 'woman', 'apple', 'banana', 'pear', 'mac', 'ubuntu', 'windown']
# add new meaning here
mean = ['nanhai', 'nanren', 'nvhai', 'nvren', 'pinguo', 'xiangjiao', 'pingguodiannao', 'linuxxitong', 'laji']

for cid, src, dest in course_info:
	for i in range(1, 5):
		lesson = '''\nlesson = Lesson(course_id=%d,
			lesson_id=%d,
			lesson_title=\'%s\', 
			author=\'%s\',
			difficulty='beginner',
			source_language=\'%s\',
			destination_language=\'%s\',
			entries=entry_lists,
			questions=['','',''],
			answers=['','',''],
			notes=\'%s\')

	lesson.put()\n''' % (cid, i, 'lesson-' + str(i), 'admin', src, dest, note)
		f.write(lesson)

		for j in range(1, 10-1):
			entry = '''\nentry = Entry(entry_id = %d,
			lesson_id = %d,
			imgURLs = '\'img/lesson/cn%d\',
			word = \'%s\',
			mean = \'%s\',
			source_language = \'%s\',
			destination_language = \'%s\',
			notes = \'%s\')

	entry.put()\n'''% (j, i, j, word[j], mean[j], src, dest, note)
			f.write(entry)

f.close()