for _ in range(int(input())):
    n,m=[str(t) for t in input().split()]
    print(int(str(int(n[::-1])+int(m[::-1]))[::-1]))
