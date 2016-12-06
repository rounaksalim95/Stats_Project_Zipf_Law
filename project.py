import glob 
import itertools 
import collections

def analyze(file): 
	f = open(file, 'r')
	words = [word for line in f for word in line.split()]
	print "The total word count is : ", len(words)
	# Use collections.Counter 
	c = collections.Counter(words)
	for word, count in c.most_common(5):
		print word, (count * 1.0)/len(words)

def main(): 
	list_of_files = glob.glob('./*.txt')
	list_of_frequencies = []
	for file in list_of_files: 
		list_of_frequencies.append(analyze(file))



if __name__ == "__main__":
	main()