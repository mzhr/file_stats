import os


def remove_stopwords(data):

	# Get file with stopwords
	directory = os.getcwd() + '/data/stopwords.txt'

	# Open the file with the stopwords
	try:
		stop_word = open(directory, 'r')
	except IOError as e:
		print("I/O error({0}): {1} '{2}'".format(
			e.errno, e.strerror, directory))
		sys.exit()

	# Get words from stopwords file
	stop_words = []
	for word in stop_word:
		stop_words.append(word)

	# Remove stopwords from the data
	new_data = {} 
	for key, value in data.iteritems():
		if key + '\n' not in stop_words:
			new_data[key] = value

	return new_data


def remove_nonalpha(data):

	# Remove non alpha words
	new_data = {}
	for key, value in data.iteritems():
		if key.isalpha():
			new_data[key] = value

	return new_data

