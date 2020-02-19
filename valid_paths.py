import numpy as np
import numpy.random as nr
import sys
import copy

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

# def gen_sets(n,k):#k is the number of points, n is the number of sets
# 	# Returns a list[] of k-tuples() of disjoint subsets
# 	if(n<k):
# 		return []
# 	elif(n==k):
# 		return [tuple([{i+1} for i in range(n)])]
# 	else:
# 		pass

# def stirling_partitions(n,k): # Returns a list X of tuples, st each tuple in X is a partitions of the form ({1,2},{3},{4,5})
# 	# Base cases
# 	if (n == 0 or k == 0 or k > n): 
# 		return []
# 	if (k == 1): 
# 		s = {i+1 for i in range(n)}
# 		return [(s,)]
# 	if (k==n):
# 		return [({i},) for i in range(n)]

# 	# S(n+1, k) = k*S(n, k) + S(n, k-1) 

# 	#case 1 : singleton {n}
# 	prev = stirling_partitions(n,k-1)
# 	stn = [  ]




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

	# lst = gen_sets(5,4)
	# print(*lst,sep="\n")
if __name__ == "__main__":
	main()