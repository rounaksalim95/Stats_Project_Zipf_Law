import glob 
import itertools 
import collections

NUMBER_OF_WORDS = 5
NUMBER_OF_BOOKS = 41


def analyze(file): 
	f = open(file, 'r')
	words = [word for line in f for word in line.split()]
	print "The total word count is : ", len(words)
	# Use collections.Counter 
	c = collections.Counter(words)
	counter_freq = []
	for word, count in c.most_common(NUMBER_OF_WORDS):
		first = (count * 1.0)/len(words) * 100
		counter_freq.append(first)
		print word, first  

	first = counter_freq[0]
	print " Zipf's law values : ", first, first/2, first/3, first/4, first/5 
	return counter_freq



def main(): 
	list_of_files = glob.glob('./*.txt')
	list_of_frequencies = []
	frequency_sum = [0] * NUMBER_OF_WORDS
	for file in list_of_files: 
		list_of_frequencies.append(analyze(file))

	for i in range(len(list_of_frequencies)):
		for j in range(NUMBER_OF_WORDS): 
			frequency_sum[j] += list_of_frequencies[i][j]

	for i in range(NUMBER_OF_WORDS):
		frequency_sum[i] /= NUMBER_OF_BOOKS

	zipf_values = [0] * NUMBER_OF_WORDS
	first_avg_zipf = frequency_sum[0]   
	zipf_values[0] = first_avg_zipf

	for i in range(1, NUMBER_OF_WORDS): 
		zipf_values[i] = first_avg_zipf / (i + 1)

	print "Actual values : ", frequency_sum
	print "Zipf values : ", zipf_values



if __name__ == "__main__":
	main()