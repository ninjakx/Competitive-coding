from itertools import groupby
for _ in range(int(input())):
    u=[]
    s=[len(str(t)) for t in input().split()]
    for k ,g in groupby(s):
        
        u.append(len(list(g)))
    print(max(u))
    

