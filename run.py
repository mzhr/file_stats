import sys
from src import parser, grapher, analyser

def main(argv):
	# Deal with the command line options
	run = commandline_options(argv)
	if run == False:
		sys.exit()

	# Open files and parse through text data, remove nonalpha words, 
	# remove stopwords, then draw the graph.
	parsed_data = parser.parse(argv)
	alpha_data = analyser.remove_nonalpha(parsed_data)
	word_data = analyser.remove_stopwords(alpha_data)
	grapher.create_graph(word_data)

def commandline_options(argv):
	
	if len(argv) == 0:
		print "Enter files after calling program"
		return False

if __name__ == "__main__":
	main(sys.argv[1:])

