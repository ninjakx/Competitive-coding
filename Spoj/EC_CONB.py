for _ in range(int(input())):
    s=str(input())
    if int(s)%2==0:
        d=int(bin(int(s))[:1:-1],2)
        print(d)
    else:
        print(s)
       

