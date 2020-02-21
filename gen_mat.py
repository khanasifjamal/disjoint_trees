import sys
from BitVector import BitVector 


def is_valid(bv):
	s = str(bv)
	n = len(bv)

	if(n%2 == 1):
		return False
	count = 0
	for i in range(n//2):
		x = s[2*i]+s[2*i + 1]
		if x=='01':
			count = count+1
		if x=='10':
			count = count-1
	return (count==0)


def main():
	bv = BitVector(bitstring=sys.argv[1])
	print(is_valid(bv))

if __name__ == '__main__':
	main()