for _ in range(int(input())):
    x,y=[int(t) for t in input().split()]
    if (y==x-2 or y==x):
     if x%2==0 and y%2==0 :
        print(x+y)
     elif x%2!=0 and y%2!=0:
        print(x+y-1)
    else:
        print("No Number")

