import math
for _ in range(int(input())):
    a,b=[int(t) for t in input().split()]
    u=b%4
    if b!=0:
     if u==0:
        exp=4

     else:
        exp=u
     idig=math.pow(int(str(a)[-1]),exp)
     print(int(idig%10))
    else:
        print('1')

