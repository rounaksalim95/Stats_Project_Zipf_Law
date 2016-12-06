import glob 

def analyze(file):
	f = open(file, 'r')
	return collections.Counter(itertools.chain(line.split() for line in f))



def main(): 
	list_of_files = glob.glob('./*.txt')
	list_of_frequencies = []
	for file in list_of_files: 
		list_of_frequencies.append(analyze(file))

	for freq in list_of_frequencies: 
		print max(freq, key = freq.get)



if __name__ == "__main__":
	main()