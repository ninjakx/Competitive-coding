for _ in range(int(input())):
 
    m,n=[int(t) for t in input().split()] 
    print(int(max(m*(n//2+n%2) , n*(m//2+m%2))))
