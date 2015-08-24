import sys
from src import parser

def main(argv):
	# Open files and parse thorugh text data
	data = parser.parse(argv)

if __name__ == "__main__":
	main(sys.argv[1:])
