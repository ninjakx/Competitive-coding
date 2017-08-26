for i in range(1, 1000):
	n = int(input())
	if n==0: break
	print('Case %d, N = %d, # of different labelings = %d' % (i, n, pow(n, n-2)))
