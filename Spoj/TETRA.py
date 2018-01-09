from math import sqrt

N = int(input())
for _ in range(0, N):
	w,v,u,U,V,W = map(int, input().split())
	s1 = (U+w+v)/2.0
	s2 = (W+v+u)/2.0
	s3 = (V+w+u)/2.0
	s4 = (U+V+W)/2.0
	a1 = sqrt(s1*(s1-U)*(s1-w)*(s1-v))
	a2 = sqrt(s2*(s2-W)*(s2-v)*(s2-u))
	a3 = sqrt(s3*(s3-V)*(s3-w)*(s3-u))
	a4 = sqrt(s4*(s4-U)*(s4-V)*(s4-W))
	X = (w-U+v)*(U+v+w)
	Y = (u-V+w)*(V+w+u)
	Z = (v-W+u)*(W+u+v)
	x = (U-v+w)*(v-w+U)
	y = (V-w+u)*(w-u+V)
	z = (W-u+v)*(u-v+W)
	A = sqrt(x*Y*Z)
	B = sqrt(y*Z*X)
	C = sqrt(z*X*Y)
	D = sqrt(x*y*z)
	
	vol = sqrt((-A+B+C+D)*(A-B+C+D)*(A+B-C+D)*(A+B+C-D))/(192.0*u*v*w)
	insphere = 3.0*vol/(a1+a2+a3+a4)
	print("%.4f" %insphere)
