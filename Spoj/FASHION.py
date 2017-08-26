for _ in range(int(input())):
    s=0
    n=int(input())
    m=sorted([int(t) for t in input().split()])
    w=sorted([int(t) for t in input().split()])
    for k in range(n):
        s=s+m[k]*w[k]
    print(s)
    
