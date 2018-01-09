while(1):
    a1,a2,a3=[int(t) for t in input().split()]

    if(a1==a2==a3==0):
        break
    if(a1+a3==2*a2):
        print("AP",a3+(a3-a2))
    else:
        print("GP",int(a3*(a3/a2)))
    

