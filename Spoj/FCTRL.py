for _ in range(int(input())):
    n=int(input())
    s=0
    while True:
        n=int(n/5)
        if n==0:
            break
        s=s+n
 
    print(s)
