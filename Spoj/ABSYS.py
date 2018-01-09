st='machula'
for _ in range(int(input())):
    input()
    a,_,b,_,c=[str(t) for t in input().split()]
    if st in a:
        a=str(int(c)-int(b))
    elif st in b:
        b=str(int(c)-int(a))
    elif st in c:
        c=str(int(a)+int(b))
    print(a+' + '+b+' = ',c)
    
    
