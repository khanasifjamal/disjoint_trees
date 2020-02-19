import numpy as np
import numpy.random as nr
import sys

def to_set(str):
	s = {int(i) for i in str}
	return s

def comp(tup1,tup2):
	s1 = tup1[0]
	s2 = tup1[1]
	s3 = tup2[0]
	s4 = tup2[1]
	if (len(s1 & s3) >0 and len(s2 & s4)>0) or ( len(s1 & s4)>0 and len(s2 & s3)>0 ):
		return 1
	return 0

def main():
	file_name = sys.argv[1]
	file = open(file_name,"r")
	set_strings= file.read().splitlines() # list of strings, each string is of the form '12 345' represents {1,2} {3,4,5}
	sets_tup = [tuple(i.split()) for i in set_strings] #Has tuples ('12','34')
	sets = [(to_set(tup[0]),to_set(tup[1])) for tup in sets_tup]

	n = len(sets)
	mat = np.empty((n,n),dtype=np.int_)

	for i in range(n):
		for j in range(n):
			mat[i][j] = comp(sets[i],sets[j])

	np.savetxt('mat.csv', mat, delimiter=',')
	print("matrix written to :mat.csv")
	print(mat)
	det = np.linalg.det(mat)
	rank = np.linalg.matrix_rank(mat)

	print("\nSize of the matrix        : %sx%s\n"
		"Rank of the matrix       : %s\n"
		"Determinant of the matrix : %s\n"%(n,n,rank,det))
if __name__ == "__main__":
	main()