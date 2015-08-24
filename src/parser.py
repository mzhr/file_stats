import sys


def parse(argv):
	files = open_files(argv)

	
def open_files(argv):

	# List for a list of opened files given in commandline arguement.
	files = []

	# Open all files given in arguement, 
	# catch incorrect non-existant filenames.
	for i in range(len(argv)):
		try:
			files[i] = open(argv[i], 'r')
		except IOError as e:
			print("I/O error({0}): {1} '{2}'".format(
				e.errno, e.strerror, argv[i]))
			break

	return files

