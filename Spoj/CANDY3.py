for _ in range(int(input())):
    input()
    s=0
    c=0
    size=int(input())
    for _ in range(size):
       
        n=input()
        c+=1
        if not n:
            break
        s=(s+int(n))%int(size)
        
    print("YES" if s%int(size)==0 else "NO")
    

