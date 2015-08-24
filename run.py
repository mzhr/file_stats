import sys
from src import parser, grapher

def main(argv):
	# Open files and parse thorugh text data, then draw graph
	data = parser.parse(argv)
	grapher.create_graph(data)

if __name__ == "__main__":
	main(sys.argv[1:])

