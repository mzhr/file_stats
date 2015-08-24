import matplotlib.pyplot as plt


def create_graph(data):

	# Setup data to be used for graph
	graph_words = setup_data(data)
	graph_data = {}
	for key, value in data.iteritems():
		if key in graph_words:
			graph_data[key] = value

	# Draw Graph
	plt.bar(range(len(graph_data)), graph_data.values(), align='center')
	plt.xticks(range(len(graph_data)), graph_data.keys())
	plt.show()


def setup_data(data):

	# Keep track and create a list of most used words.
	new_data = []
	word_count = 0

	while(word_count < 10):
		highest_count = 0
		highest_word = ""
		for key, value in data.iteritems():
			if highest_count < value and key not in new_data:
				highest_count = value
		for key, value in data.iteritems():
			if value == highest_count:
				new_data.append(key)
				word_count = word_count + 1

	return new_data

