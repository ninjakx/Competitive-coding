# removing duplicates
arr = [1,2,1,3,4,5]
res = []
a= {}
[res.append(i) for i in arr if i not in res]
#print(res)
#print(list(a.fromkeys(arr)) )


# removing consecutive char or string
arr = ['s','a',1,2,'d','d',1,1,3,4,5]
ar = []
for i in range(1,len(arr)):
    if ord(str(arr[i-1]))-ord(str(arr[i]))!=0:
        ar.append(arr[i-1])
print(ar)
