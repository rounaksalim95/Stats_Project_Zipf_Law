import glob 

def analyze(file):
	f = open(file, 'r')
	for word in 



def main(): 
	list_of_files = glob.glob('./*.txt')
	for file in list_of_files: 
		analyze(file)