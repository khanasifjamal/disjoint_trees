import numpy as np
import numpy.random as nr
import sys

def to_set(str):
	s = {int(i) for i in str}
	return s

def main():
	file_name = sys.argv[1]
	file = open(file_name,"r")
	set_strings= file.read().splitlines() # list of strings, each string is of the form '12 345' represents {1,2} {3,4,5}
	sets_tup = [tuple(i.split()) for i in set_strings] #Has tuples ('12','34')
	sets = [(to_set(tup[0]),to_set(tup[1])) for tup in sets_tup]

	print(sets)

if __name__ == "__main__":
	main()