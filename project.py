import glob 
import itertools 
import collections
import matplotlib.pyplot as plt

NUMBER_OF_WORDS = 5
NUMBER_OF_BOOKS = 41
Z_95_VALUE = 1.96


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

	# Get the average frequency 
	average_frequency = [0] * NUMBER_OF_WORDS
	for i in range(NUMBER_OF_WORDS):
		average_frequency[i] = frequency_sum[i] / NUMBER_OF_BOOKS

	zipf_values = [0] * NUMBER_OF_WORDS
	first_avg_zipf = average_frequency[0]   
	zipf_values[0] = first_avg_zipf

	for i in range(1, NUMBER_OF_WORDS): 
		zipf_values[i] = first_avg_zipf / (i + 1)

	print "\n==================================================================\n"

	print "Actual values : ", average_frequency, '\n'
	print "Zipf values : ", zipf_values, '\n'

	num_std_dev = [0] * NUMBER_OF_WORDS

	# Calculate the standard deviation 
	for i in range(len(list_of_frequencies)):
		for j in range(len(list_of_frequencies[i])):
			num_std_dev[j] += (list_of_frequencies[i][j] - average_frequency[j]) ** 2

	print "Numerator is : ", num_std_dev, '\n'

	std_dev = [0] * NUMBER_OF_WORDS
	for i in range(len(num_std_dev)):
		std_dev[i] = (num_std_dev[i] / (NUMBER_OF_BOOKS - 1)) ** 0.5

	print "Standard deviation is : ", std_dev, '\n'
		
	# Calculate the p values for each word
	z = [0] * NUMBER_OF_WORDS

	for i in range(NUMBER_OF_WORDS):
		#z_numerator = (zipf_values[i] - average_frequency[i])
		z_numerator = (average_frequency[i] - zipf_values[i])
		z_denominator = std_dev[i] / (NUMBER_OF_BOOKS ** 0.5)
		z[i] = z_numerator / z_denominator

	print "Z values are : ", z, '\n'

	zipfian_ratios = [1.0/1, 1.0/2, 1.0/3, 1.0/4, 1.0/5]

	actual_ratios = [0] * NUMBER_OF_WORDS

	for i in range(NUMBER_OF_WORDS):
		actual_ratios[i] = average_frequency[i] / average_frequency[0]

	print "Actual ratios are : ", actual_ratios, '\n'
	print "Zipfian rations are : ", zipfian_ratios, '\n'


	plt.plot([1,2,3,4,5], zipfian_ratios)
	plt.plot([1,2,3,4,5], actual_ratios)
	plt.show()


if __name__ == "__main__":
	main()