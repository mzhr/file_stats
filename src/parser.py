import sys


def parse(argv):

	# Parse each file and return a dictionary of a statistical count of 
	# all encountered words.
	files = open_files(argv)
	text_data = parse_data(files)
	return text_data


def open_files(argv):

	# List for a list of opened files given in commandline arguement.
	files = []

	# Open all files given in arguement, 
	# catch incorrect non-existant filenames.
	for i in range(len(argv)):
		try:
			f = open(argv[i], 'r')
			files.append(f)
		except IOError as e:
			print("I/O error({0}): {1} '{2}'".format(
				e.errno, e.strerror, argv[i]))
			sys.exit()

	return files


def parse_data(files):

	# Dictionary for each word to be counted as dictionary is a key pair, 
	# or in this case, count, relation.
	text_data = {}
	
	# For each of the files, read each word and add to dictionary.
	# Keyword 'file' cannot be used.
	for f in files:
		for line in f:
			words = line.split()
			for word in words:
				word = word.lower()
				if word not in text_data:
					text_data[word] = 1
				else: 
					text_data[word] = text_data[word] + 1

	return text_data

