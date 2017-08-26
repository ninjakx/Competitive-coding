from math import factorial
while(1):
	n,d=[int(t) for t in input().split()]
	if n==0 and d==0:
		break
	print(n**d)

