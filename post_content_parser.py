import re

groups_file = tuple(open('groups_list.txt', 'r+'))
groups_list = [ ]

delete = re.compile(u'\W+?', re.UNICODE)

for group in groups_file:
	groups_list.append(int(group.replace('\n', '')))

for group in groups_list:
	#posts_list - лист идшников последних 100 постов группы group
	print('Group:' + str(group))
	posts_file = tuple(open('groups_posts/' + str(group), 'r+'))
	posts_list = [ ]

	for post in posts_file:
		posts_list.append(int(post.replace('\n', '')))

	#print(posts_list)

	# начинаем работу с файлами постов и вычленением из них текста

	out = open('out', 'w+')

	for post in posts_list:
		post_data_file = open('posts_data/' + str(group) + '/' + str(post), 'r+')
		all_post_data = post_data_file.read()
		#print(post_data_file.read().encode('windows-1251'))
		#print(all_post_data)
		try:
			post_data_text = re.findall(r'\'text\':(.*?),', str(all_post_data))			
			post_data_text = str(post_data_text)
			post_data_text = post_data_text.replace("<br>", " ")
			
			post_data_text = delete.sub(' ', post_data_text)

			#print(re.sub(r'\s', '', post_data_text), end = "\n")
			print(post_data_text.split())
		except Exception as e:
			print(e)
			#pass